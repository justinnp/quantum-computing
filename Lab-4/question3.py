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
        # starter code:
        # QuantumCircuit with V quantum registered bits and V classically registered bits
        # Superposition state over all qubits

        # each Uc (problem hamiltonian, parameterized by gamma) and Ub (mixing/driver unitary, parameterized by beta) is in a single layer (p = 1)
        for layer in range(p):
            # nodes on connected edge
            for n, n_next in self.E:
                # apply hamiltonian unitary (CNOT + RZ(gamma) + CNOT) to each qubit corresponding to each edge connected node 
                self.qaoa_circuit.cx(n, n_next)
                self.qaoa_circuit.rz(2 * self.gamma, n_next)
                self.qaoa_circuit.cx(n, n_next)
            # apply mixing unitary (Ub) on all qubits (nodes)
            for q in range(len(self.V)):
                self.qaoa_circuit.rx(2 * self.beta, q)

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

        # cut string represents the set of nodes present on either side of the cut

        for n, n_next in self.E:
            # in lecture, a graph of edges [[0,1], [1,2]] was cut resulting in '010' and '101'
            # this translates to qubits 0 and 2 being in partition '0' and qubit 1 being in partition '1' for 010, cut value of 2 and 1 respectively, max = 2
            # compare parition integers and add to overall cut value
            if  s[n] != s[n_next]:
                # cut value represents the number of edges between two sides of the cut
                cut_value += 1
    
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