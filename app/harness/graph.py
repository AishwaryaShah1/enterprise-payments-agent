from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from .state import InvestigationState
from .nodes import (
    parse_request,
    gather_metrics,
    analyze_case,
    respond,
)


def build_graph():

    graph = StateGraph(InvestigationState)

    graph.add_node(
        "parse_request",
        parse_request,
    )

    graph.add_node(
        "gather_metrics",
        gather_metrics,
    )

    graph.add_node(
        "analyze_case",
        analyze_case,
    )

    graph.add_node(
        "respond",
        respond,
    )

    graph.add_edge(
        START,
        "parse_request",
    )

    graph.add_edge(
        "parse_request",
        "gather_metrics",
    )

    graph.add_edge(
        "gather_metrics",
        "analyze_case",
    )

    graph.add_edge(
        "analyze_case",
        "respond",
    )

    graph.add_edge(
        "respond",
        END,
    )

    return graph.compile()


payments_graph = build_graph()