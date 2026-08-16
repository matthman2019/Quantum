from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(
    channel="ibm_quantum_platform",
    token="VCOTZ6Gp-lC87iRtXuO7UEYHw4ZOz2tKlxV7jMZpokmv", 
    overwrite=True, 
    instance="crn:v1:bluemix:public:quantum-computing:us-east:a/407ca19e17a241c49d094e4d01c47f57:61b62a1b-fdd6-4425-92d0-502f8dd00f40::", 
    set_as_default=True
)
