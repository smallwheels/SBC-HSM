# SBC-HSM
# Coventry University - Ethical Hacking and Cyber Security (Bsc) Final Year Project
Hardware Security Modules (HSM) are commonly used to increase data security by containing a number of cryptographic functions (such as encryption / decryption) in a separate physical computing device that can be hardened and tamper resistant.
This project will be investigating the functionality necessary to create a HSM using SBCs for generating cryptographic material and does not review the efficacy of any given SBC security or system hardening.
#
The following repository is a Python Hardware Security Module (HSM) designed to be ran a Single Board Computer (SBC) that is able to encrypted / decrypted in **AES-256**, **AES-128** and **3DES**, in addtion to **hashing** and **HMAC** functions. These functions are selected through a CLI based user interface inadditon to key generation for each given algorithm.
