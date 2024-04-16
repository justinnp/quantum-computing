OPENQASM 2.0;
include "qelib1.inc";
qreg q[6];
creg c[6];

h q[0];
h q[1];
h q[5];
cu1(pi/32) q[0],q[5];
cu1(pi/16) q[1],q[5];
cu1(pi/8) q[2],q[5];
cu1(pi/4) q[3],q[5];
cu1(pi/2) q[4],q[5];
swap q[0],q[5];
swap q[1],q[4];
swap q[2],q[3];