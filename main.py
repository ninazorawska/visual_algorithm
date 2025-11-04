import random
from typing import List, Generator, Tuple, Dict, Any
import streamlit as st
import networkx as nx
import numpy as np

# -----------------------------
# Helpers: session state
# -----------------------------
def init_state():
    ss = st.session_state
    ss.setdefault("algo_family", "Sorting")
    ss.setdefault("sorting_algo", "Bubble Sort")
    ss.setdefault("graph_algo", "DFS")
    ss.setdefault("array_size", 15)
    ss.setdefault("array", None)
    ss.setdefault("graph", None)
    ss.setdefault("start_node", 0)
    ss.setdefault("generator", None)
    ss.setdefault("current_step", None)  # payload describing the current visualization step
    ss.setdefault("visited", set())
    ss.setdefault("frontier", [])
    ss.setdefault("pos", None)  # graph layout cache

init_state()

# -----------------------------
# Sorting algorithms (generators)
# Each yields a dict describing the step to render.
# -----------------------------
def bubble_sort_steps(arr: List[int]) -> Generator[Dict[str, Any], None, None]:
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            # compare j and j+1
            yield {"type": "compare", "i": j, "j": j+1, "array": a[:]}
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                yield {"type": "swap", "i": j, "j": j+1, "array": a[:]}
    yield {"type": "done", "array": a[:]}

def insertion_sort_steps(arr: List[int]) -> Generator[Dict[str, Any], None, None]:
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        yield {"type": "pick", "i": i, "array": a[:]}
        while j >= 0 and a[j] > key:
            yield {"type": "shift", "from": j, "to": j+1, "array": a[:]}
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        yield {"type": "insert", "pos": j+1, "array": a[:]}
    yield {"type": "done", "array": a[:]}

SORTING_IMPL = {
    "Bubble Sort": bubble_sort_steps,
    "Insertion Sort": insertion_sort_steps,
}

# -----------------------------
# Graph algorithms (generators)
# Yield visited/frontier at each step.
# -----------------------------
def dfs_steps(G: nx.Graph, start: int) -> Generator[Dict[str, Any], None, None]:
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        yield {"type": "pop", "node": node, "visited": visited.copy(), "stack": stack[:]}
        if node not in visited:
            visited.add(node)
            yield {"type": "visit", "node": node, "visited": visited.copy(), "stack": stack[:]}
            # push neighbors in reverse for deterministic order
            neigh = sorted(list(G.neighbors(node)), reverse=True)
            stack.extend([n for n in neigh if n not in visited])
            yield {"type": "push_neighbors", "added": neigh, "visited": visited.copy(), "stack": stack[:]}

    yield {"type": "done", "visited": visited.copy(), "stack": []}

def bfs_steps(G: nx.Graph, start: int) -> Generator[Dict[str, Any], None, None]:
    visited = set([start])
    queue = [start]
    yield {"type": "enqueue_start", "visited": visited.copy(), "queue": queue[:]}

    while queue:
        node = queue.pop(0)
        yield {"type": "dequeue", "node": node, "visited": visited.copy(), "queue": queue[:]}

        for n in sorted(list(G.neighbors(node))):
            if n not in visited:
                visited.add(n)
                queue.append(n)
                yield {"type": "discover", "node": n, "visited": visited.copy(), "queue": queue[:]}

    yield {"type": "done", "visited": visited.copy(), "queue": []}

GRAPH_IMPL = {
    "DFS": dfs_steps,
    "BFS": bfs_steps,
}

# -----------------------------
# UI: Sidebar controls
# -----------------------------
st.set_page_config(page_title="Algorithm Visualizer", page_icon="🧠", layout="wide")
st.title("🧠 Algorithm Visualizer")

with st.sidebar:
    st.header("Controls")
    st.session_state.algo_family = st.selectbox("Category", ["Sorting", "Graphs"], index=0)

    if st.session_state.algo_family == "Sorting":
        st.session_state.sorting_algo = st.selectbox("Algorithm", list(SORTING_IMPL.keys()))
        st.session_state.array_size = st.slider("Array size", 5, 50, st.session_state.array_size)
        seed = st.number_input("Random seed", value=42, step=1)
        speed = st.slider("Playback delay (ms)", 0, 1000, 150)
        if st.button("🔁 New Array"):
            random.seed(int(seed))
            st.session_state.array = random.sample(range(5, 100), st.session_state.array_size)
            st.session_state.generator = None
            st.session_state.current_step = None

    else:
        st.session_state.graph_algo = st.selectbox("Traversal", list(GRAPH_IMPL.keys()))
        n_nodes = st.slider("Nodes", 5, 30, 10)
        prob = st.slider("Edge probability (Erdős–Rényi)", 0.05, 0.6, 0.2)
        seed = st.number_input("Random seed", value=7, step=1)
        speed = st.slider("Playback delay (ms)", 0, 1000, 150)
        if st.button("🔁 New Graph"):
            rng = np.random.default_rng(int(seed))
            G = nx.erdos_renyi_graph(n_nodes, prob, seed=int(seed))
            # ensure connected start component (if empty graph, regenerate once)
            if len(G) == 0 or n_nodes == 0:
                G = nx.erdos_renyi_graph(n_nodes, prob, seed=int(seed) + 1)
            st.session_state.graph = G
            st.session_state.start_node = 0 if 0 in G.nodes else list(G.nodes)[0]
            st.session_state.pos = nx.spring_layout(G, seed=int(seed))
            st.session_state.generator = None
            st.session_state.current_step = None

# -----------------------------
# Main area: Visuals
# -----------------------------
colL, colR = st.columns([3, 2], gap="large")

# Sorting view
def render_array(step: Dict[str, Any], height=220):
    a = step["array"]
    idx_highlight = {k for k in ["i", "j", "from", "to", "pos"] if k in step}
    highlights = set([step[k] for k in idx_highlight if isinstance(step[k], int)])
    if "i" in step and "j" in step:
        highlights.update({step["i"], step["j"]})

    st.caption(f"Step: {step['type']}")
    # Draw bars
    maxv = max(a) if a else 1
    bar_width = max(6, int(600 / max(1, len(a))))
    # Render as unicode bars + simple HTML for emphasis (lightweight, no external charts)
    bar_html = "<div style='display:flex;align-items:flex-end;gap:4px;height:{}px;'>".format(height)
    for idx, val in enumerate(a):
        h = int((val / maxv) * (height - 30)) + 10
        bg = "#7fb3ff" if idx in highlights else "#d0d7de"
        bar_html += f"<div title='{val}' style='width:{bar_width}px;height:{h}px;background:{bg};border-radius:4px;'></div>"
    bar_html += "</div>"
    st.markdown(bar_html, unsafe_allow_html=True)

# Graph view
def render_graph(G: nx.Graph, step: Dict[str, Any], pos):
    st.caption(f"Step: {step['type']}")
    visited = set(step.get("visited", []))
    frontier = step.get("stack", step.get("queue", [])) or []
    # Build node color tags (no explicit colors, just labels next to nodes)
    labels = {}
    for n in G.nodes:
        tag = []
        if n in visited: tag.append("V")
        if n in frontier: tag.append("F")
        labels[n] = f"{n}{' [' + ','.join(tag) + ']' if tag else ''}"

    # Use Streamlit's built-in graphviz-ish network via nx adjacency drawn as text fallback:
    # Lightweight HTML render: list edges and annotate visited/frontier.
    with st.container(border=True):
        st.write("**Nodes**:", ", ".join(labels[n] for n in G.nodes))
        st.write("**Edges**:", ", ".join(f"({u}–{v})" for u, v in G.edges))
        if "node" in step:
            st.write(f"**Focus node**: {step['node']}")
        if "added" in step:
            st.write(f"**Neighbors considered**: {step['added']}")

# -----------------------------
# Orchestrate run/step controls
# -----------------------------
def get_generator():
    if st.session_state.algo_family == "Sorting":
        arr = st.session_state.array
        if arr is None:
            st.session_state.array = random.sample(range(5, 100), st.session_state.array_size)
            arr = st.session_state.array
        return SORTING_IMPL[st.session_state.sorting_algo](arr)
    else:
        G = st.session_state.graph
        if G is None:
            G = nx.erdos_renyi_graph(10, 0.2, seed=7)
            st.session_state.graph = G
            st.session_state.pos = nx.spring_layout(G, seed=7)
        start = st.session_state.start_node if st.session_state.start_node in G.nodes else list(G.nodes)[0]
        return GRAPH_IMPL[st.session_state.graph_algo](G, start)

with colR:
    st.subheader("Controls")
    run_col1, run_col2, run_col3 = st.columns(3)
    if run_col1.button("▶️ Step"):
        if st.session_state.generator is None:
            st.session_state.generator = get_generator()
        try:
            st.session_state.current_step = next(st.session_state.generator)
        except StopIteration:
            st.session_state.current_step = {"type": "done"}
    if run_col2.button("⏭️ Run 5 steps"):
        if st.session_state.generator is None:
            st.session_state.generator = get_generator()
        for _ in range(5):
            try:
                st.session_state.current_step = next(st.session_state.generator)
            except StopIteration:
                st.session_state.current_step = {"type": "done"}
                break
    if run_col3.button("🔄 Reset"):
        st.session_state.generator = None
        st.session_state.current_step = None

with colL:
    if st.session_state.algo_family == "Sorting":
        st.subheader(f"Sorting • {st.session_state.sorting_algo}")
        if st.session_state.current_step is None:
            st.info("Click **Step** to begin.")
            # Render initial array
            arr = st.session_state.array or random.sample(range(5, 100), st.session_state.array_size)
            render_array({"type": "init", "array": arr})
        else:
            render_array(st.session_state.current_step)

        with st.expander("What you’re seeing"):
            st.markdown("""
            - **compare**: highlight two elements being compared  
            - **swap/shift/insert**: shows mutation steps  
            - **done**: algorithm finished (array sorted)
            """)

    else:
        st.subheader(f"Graphs • {st.session_state.graph_algo}")
        G = st.session_state.graph
        if G is None:
            G = nx.erdos_renyi_graph(10, 0.2, seed=7)
            st.session_state.graph = G
            st.session_state.pos = nx.spring_layout(G, seed=7)
        step = st.session_state.current_step or {"type": "ready", "visited": [], "queue": []}
        render_graph(G, step, st.session_state.pos)

        with st.expander("What you’re seeing"):
            st.markdown("""
            - **DFS**: LIFO stack; go deep before backtracking  
            - **BFS**: FIFO queue; explore neighbors level by level  
            - We annotate nodes as **V** (visited) and **F** (in frontier).
            """)

st.markdown("---")
st.caption("Tip: Pin this repo and add a README with setup + screenshots.")
