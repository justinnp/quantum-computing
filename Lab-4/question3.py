import numpy as np
import networkx as nx
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.providers.aer import QasmSimulator


class QAOASolver(object):
    def __init__(self, input_graph: nx.Graph, num_shots=1000):
        self.G = input_graph
        self.E = list(input_graph.edges())
        self.V = list(input_graph.nodes())
        self.gamma = np.random.uniform()
        self.beta = np.random.uniform()
        self.simulator = QasmSimulator()
        self.num_shots = num_shots
        self.qaoa_solution = 0

    def create_qaoa_circuit(self, p: int=1):
        """
        Creates QAOA circuit self.qaoa_circuit for graph self.G of p layers
        Args:
            p: int, the number of layers of QAOA circuit
        Return:
            None
        """

        self.qaoa_circuit = QuantumCircuit(len(self.V), len(self.V))
        self.qaoa_circuit.h(range(len(self.V)))
        ############################################################################
        # Student code begin
        ############################################################################

        raise NotImplementedError(
                "`create_qaoa_circuit` function in "
                + "`question3.py` needs to be implemented"
            )
        
        ############################################################################
        # Student code end
        ############################################################################

    def execute_qaoa_circuit(self):
        self.qaoa_circuit.measure(range(len(self.V)),range(len(self.V)))
        compiled_circuit = transpile(self.qaoa_circuit, self.simulator)
        job = self.simulator.run(compiled_circuit, shots=self.num_shots)
        result = job.result()
        self.qaoa_counts = result.get_counts(compiled_circuit)

    def find_maxcut(self):
        for s in self.qaoa_counts:
            self.qaoa_solution = max(self.qaoa_solution, self._compute_cut(s))

    def _compute_cut(self, s: str):
        """
        Computes the cut value of cut/partition string s (little-endian) of graph self.G
        Args:
            s: str, the string of cut/partition of nodes in little-endian order
        Return:
            cut_value: int
        """

        cut_value = 0
        s = s[::-1]
        ############################################################################
        # Student code begin
        ############################################################################

        raise NotImplementedError(
                "`_compute_cut` function in "
                + "`question3.py` needs to be implemented"
            )
        
        ############################################################################
        # Student code end
        ############################################################################
        
        return cut_value

    def optimize_parameters(self):
        pass

    def solve(self):
        self.create_qaoa_circuit()
        self.execute_qaoa_circuit()
        self.find_maxcut()
        return self.qaoa_solution