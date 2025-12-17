# Adrián Constante

Backend Developer | DevOps | CloudOps | Data Engineer

## Contact

- Email: <ad_con.reload@proton.me>
- LinkedIn: <https://linkedin.com/in/adrian-constant>
- GitHub: <https://github.com/adcondev>

## Professional Summary

DevOps Engineer & Go Developer with a strong foundation in Biomedical Engineering and Computer Science. Expert in architecting high-concurrency backend systems and distributed cloud infrastructure, with a specialized focus on Hardware Abstraction Layers and IoT Integration. Proven track record of engineering production-ready libraries (e.g., "Poster") that decouple complex hardware protocols from business logic, significantly reducing integration latency. Experienced in designing robust CI/CD pipelines, automating cross-platform testing, and managing self-hosted PaaS environments using Docker and Traefik. Adept at bridging the gap between low-level hardware constraints and high-level cloud architectures, delivering scalable solutions for industries ranging from retail POS systems to scientific research at CERN. Passionate about Open Source, Clean Architecture, and Test-Driven Development.

## Technologies and Tools

## Experience

## Education

## Major Projects

### Poster: Enterprise Thermal Printing Engine & Driver SDK (2025)

- **System Architecture:** Architected a modular **Go (1.24+)** library utilizing **Interface-Driven Design** and **Facade Patterns** to decouple business logic from hardware protocols. Designed a versioned **JSON Schema** middleware that validates and transforms structured data into binary ESC/POS commands, reducing client integration time by **[Pending: XX%]**.
- **Low-Level Engineering:** Engineered a custom **Windows Print Spooler** integration using `syscall` and `unsafe` to manage kernel-level print jobs. Implemented a "Force Flush" algorithm that bypasses standard spooler buffering, reducing print-start latency by **[Pending: XX%]** compared to legacy drivers.
- **Algorithm Design:** Developed a dependency-free **Graphics Engine** implementing **Atkinson Dithering** and **Bilinear Interpolation** to optimize image rendering for 1-bit thermal heads. Created a **Dynamic Table Engine** for algorithmic text wrapping and alignment, eliminating the need for manual pixel counting in receipt layouts.
- **DevOps & Security:** Established a **Tier-1 CI/CD Pipeline** using **GitHub Actions**, automating **Semantic Versioning**, **Trivy** vulnerability scanning, and multi-OS testing. Achieved **[Pending: XX%]** code coverage (verified via Codecov) and automated dependency updates using **Dependabot**.
- **Tooling & Emulation:** Designed a **Visual Emulator** that renders print jobs as PNGs, enabling a **Test-Driven Development (TDD)** approach for hardware integrations. This simulation layer allowed for **[Pending: XX%]** faster feature validation without requiring physical devices.

### Local n8n Automation Infrastructure (2025)

- *Infrastructure Engineering:* Architected a decoupled **Docker Compose** environment to orchestrate **n8n** and **ngrok**, utilizing private bridge networks to expose local services to public webhooks.
- *DevOps & Security:* Implemented **Infrastructure as Code (IaC)** and **12-Factor App** standards, securing API keys via `.env` isolation and ensuring **[Pending: XX%]** faster development cycles by simulating production environments locally.
- *Data Reliability:* Configured persistent Docker volumes to maintain state for **[Pending: Number of Workflows]** automation workflows, ensuring data integrity across container restarts and updates.
- *Workflow Automation:* Deployed this infrastructure to develop and test complex integration pipelines involving **[Pending: Specific APIs e.g., Stripe, Slack, etc.]**, effectively replacing the need for paid cloud VPS instances during the development phase.

### Printer Daemon (2025): Go WebSocket Middleware for POS Hardware

- *System Architecture:* Architected a concurrent **WebSocket server** in **Go (1.24+)** using `gorilla/websocket`, implementing thread-safe connection management (Mutex/Channels) to enable bidirectional communication between web clients and local hardware.
- *Hardware Optimization:* Engineered a custom **Hardware Abstraction Layer (HAL)** for ESC/POS protocols, developing a "Force Flush" algorithm to bypass Windows Print Spooler buffering, reducing print start latency by **[Pending: XX%]**.
- *Dynamic Templating:* Designed a **JSON-driven layout engine** that decouples business logic from rendering, allowing automatic content adaptation for distinct paper widths (58mm/80mm) and reducing client configuration time by **[Pending: XX%]**.
- *DevOps & Tooling:* Standardized the build and release lifecycle using **Taskfile**, automating binary compilation and unit testing to ensure consistent deployment across **[Pending: Number]** Windows terminals.

### Scale Daemon (2025): Industrial IoT Middleware & Windows Service

- *System Engineering:* Architected a decoupled **Windows Service** in **Go (1.24+)** to bridge industrial scales (RS232) with web clients, utilizing **WebSockets** and Go concurrency primitives (Channels, Mutex) to achieve **[Pending: XXms]** real-time data latency.
- *Resilience & Reliability:* Implemented a fault-tolerant serial communication layer using `go-serial`, featuring automatic reconnection and noise filtering to ensure **[Pending: 99.X%]** uptime in unstable hardware environments.
- *DevOps & Tooling:* Engineered a self-contained distribution pipeline using **Taskfile**, resulting in a custom **TUI Installer** (Bubbletea) that reduces on-site deployment time by **[Pending: XX%]** through automated service lifecycle management.
- *Configuration Management:* Designed a thread-safe hot-reload mechanism allowing dynamic switching of hardware drivers and ports without service interruption, facilitating support for **[Pending: Number of brands/models]** distinct scale manufacturers.

### POS Daemon (2025): Go Middleware for Thermal Printing

- *System Architecture:* Architected a protocol-agnostic middleware in **Go (1.24+)** using interface-driven design, decoupling business logic from hardware constraints to support multiple printer profiles (58mm/80mm) and protocols (ESC/POS).
- *Hardware Integration:* Engineered a custom **Hardware Abstraction Layer (HAL)** and **Windows Print Spooler** connector, ensuring reliable job queuing and reducing print failures by **[Pending: XX%]** through robust error handling.
- *Algorithm Engineering:* Implemented **Floyd-Steinberg dithering** algorithms to optimize bitmap rendering for 1-bit thermal heads, enabling high-fidelity logo printing with **[Pending: minimal/low]** memory overhead.
- *Template Engine:* Designed a **JSON-driven template system** to generate dynamic receipts, separating layout from logic; this reduced client customization time by **[Pending: XX%]** by eliminating the need for recompilation.
- *DevOps & CI/CD:* Established automated build and test pipelines using **GitHub Actions**, validating code stability across **[Pending: Number]** distinct environments/configurations prior to release.

### Snippet Box (2024): Secure Code Repository and Web Server

- *Backend Engineering:* Architected a secure, self-hosted web application using *Go (v1.22+)* and *MySQL*, utilizing `httprouter` and custom middleware for observability and security (CSRF protection, TLS 1.3, bcrypt hashing).
- *DevOps & Automation:* Established a DevOps workflow using *GitHub Actions* for CI/CD automation and *Taskfile* for build scripting. Containerized application using *Docker/Docker Compose* for consistent environments.
- *Infrastructure & Deployment:* Deployed application to *DigitalOcean Droplets* behind a *Traefik* reverse proxy, ensuring 99.9% uptime and sub-100ms response times for personal data management.
- *Database Management:* Designed a normalized MySQL schema with optimized indexing for efficient data retrieval, handling [Pending: X number of records/transactions].

### Yalemi API (2023): Scalable Social Media Backend

- *Backend Architecture:* Architected a high-performance REST API using **FastAPI** and **Python 3.10+**, implementing asynchronous I/O to handle **[Pending: X request volume or concurrent users]** with minimal latency.
- *Data Engineering:* Designed a normalized **PostgreSQL** schema using **SQLModel**, optimizing complex SQL queries (Joins/Selects) to achieve **[Pending: XXms]** query performance for voting and content retrieval.
- *Security & Auth:* Implemented a production-grade **OAuth2** authentication system with **JWT** and **Bcrypt** hashing, ensuring stateless and secure session management for user data.
- *DevOps & CI/CD:* Engineered an automated release pipeline using **GitHub Actions**, managing **Semantic Versioning** and changelogs to streamline the deployment lifecycle across **[Pending: Number of releases/commits]**.

### Low-Level LSTM and FPGA Bridge (2022): Recurrent Neural Network Implementation

- *Algorithm Engineering:* Engineered a dependency-free **LSTM Neural Network** in **Python** and **NumPy**, manually implementing **Backpropagation Through Time (BPTT)** and the **Adam Optimizer** to achieve **[Pending: XX%]** accuracy in character-level text generation.
- *Data Engineering:* Built a robust ETL pipeline using **Pandas** to process **[Pending: Number of Records]** raw text entries, handling one-hot encoding and sequence padding to optimize matrix vectorization and training throughput.
- *Hardware Deployment:* Architected a model serialization layer to export trained weights as **.coe (Coefficient)** files, facilitating the deployment of software-trained models onto **Xilinx FPGA** block memory for hardware acceleration.
- *Performance Optimization:* Implemented vectorized matrix operations for LSTM gating mechanisms (Forget, Input, Output), reducing computational overhead by **[Pending: XX%]** compared to iterative loop approaches.

### Py-Neumann (2021): Von Neumann Architecture Simulator

- *System Architecture:* Architected a modular simulation of computer hardware using **Python 3** and **OOP** (Multiple Inheritance), decoupling CPU, Memory, and I/O logic to accurately model the **Fetch-Decode-Execute** cycle.
- *Data Engineering:* Implemented efficient memory state management using **NumPy** for grid manipulation and **Pandas** for structured debugging logs, visualizing 100 memory addresses and register states in real-time.
- *Interpreter Design:* Developed a custom machine code interpreter and file parser to execute distinct opcodes (Arithmetic, Control Flow, Data Movement), translating raw text input into executable CPU instructions.
- *DevOps & Quality Assurance:* [Pending: Implemented automated testing/linting pipelines using GitHub Actions to ensure logic correctness across CPU cycles].
- *Distribution:* [Pending: Containerized application logic or created standalone executables to facilitate cross-platform educational deployment].

### Physio-Key-Gen (2020): Biometric Cryptographic Protocol

- *Algorithm Engineering:* Engineered a custom **Bloom Filter** implementation in **Python 3** using `bitarray`, optimizing set reconciliation for distributed sensor nodes with a targeted **[Pending: 0.XX%]** false positive rate.
- *Data Pipeline:* Architected a signal processing pipeline using **NumPy** and **WFDB** to extract Inter-Pulse Intervals (IPI) from the MIT-BIH Arrhythmia Database, processing records with **[Pending: XXms]** latency.
- *Security Protocol:* Designed a challenge-response authentication flow utilizing **HMAC** and **SHA-1**, enabling secure key agreement without transmitting raw biometric data across the network.
- *Simulation & Modeling:* Developed a simulation environment to validate protocol robustness against noise, demonstrating successful key establishment in **[Pending: XX%]** of test cases.

### Huffman Cipher (2020): Hybrid Cryptography & Compression Engine

- *Algorithm Engineering:* Architected a hybrid **"Compress-then-Encrypt"** pipeline in **Python 3**, integrating **Huffman Coding** with a custom **RSA** implementation to achieve **[Pending: XX%]** reduction in message size prior to encryption.
- *Low-Level Implementation:* Engineered cryptographic primitives from first principles (excluding external crypto libraries), implementing **Modular Exponentiation** and the **Extended Euclidean Algorithm** to manage public/private key derivation.
- *Data Structures:* Developed custom **Priority Queues** and **Binary Trees** to handle frequency analysis and bitstream serialization, optimizing the conversion of variable-length codes into fixed encryption blocks.
- *Data Analysis:* Designed an information-theoretic analysis module to calculate **Shannon Entropy** and **Redundancy**, validating compression performance against theoretical limits for datasets up to **[Pending: File Size/Line Count]**.
- *Code Quality & DevOps:* Implemented a modular **OOP** architecture for logic encapsulation and established **[Pending: Unit Tests/CI Pipeline]** to validate the integrity of bitwise operations and mathematical correctness.

### Cliniva (2020): Decentralized Electronic Health Record System

- *Distributed Systems Architecture:* Architected a hybrid storage solution utilizing **Ethereum** for immutable metadata and **IPFS** for decentralized content, reducing on-chain storage costs by **[Pending: XX%]** via hash-pointer referencing.
- *Smart Contract Engineering:* Developed modular **Solidity** contracts with **Role-Based Access Control (RBAC)** and **OpenZeppelin** standards, implementing a "Circuit Breaker" pattern to ensure system security during critical failures.
- *Full-Stack Integration:* Bridged **Angular** frontend interfaces with the **EVM** using **Web3.js**, managing transaction signing and asynchronous state synchronization for **[Pending: Number of Users/Records]**.
- *DevOps & Testing:* Managed the smart contract lifecycle using **Truffle Suite** and **Ganache** for local simulation, executing automated migration scripts and unit tests to ensure logical correctness prior to deployment.

### Matrix Petri Net Simulator (2025): Discrete Event System Engine

- *Algorithm Engineering:* Architected a matrix-based simulation engine in **Python 3**, translating formal mathematical tuples $(P, T, Pre, Post, M_0)$ into an executable **Object-Oriented** system to model concurrent processes.
- *Data Engineering & Optimization:* Implemented **vectorized state transitions** using **NumPy**, utilizing Pre/Post-incidence matrices to replace nested loops; this optimized the "firing rule" calculation logic by **[Pending: XX%]** compared to iterative approaches.
- *System Architecture:* Designed a robust **Command Line Interface (CLI)** and continuous simulation loop that dynamically identifies enabled transitions and performs automatic **deadlock detection** to ensure system stability.
- *DevOps & Quality Assurance:* **[Pending: Established automated testing pipelines using GitHub Actions to validate matrix logic and transition integrity across distinct network topologies].**

### A* 8-Puzzle Solver (2019): Heuristic Search Engine

- *Algorithm Engineering:* Engineered a dependency-free **A* (A-Star)** search algorithm in **Python 3**, implementing the `f(n) = g(n) + h(n)` cost function to solve optimization problems with **[Pending: XX%]** greater efficiency than non-heuristic methods (BFS/DFS).
- *Data Structures:* Architected a custom **Priority Queue** (`BestFirst`) and **Hash-based Closed Set** (`ColaQ`) to manage state space, implementing cycle detection to reduce memory overhead by **[Pending: XX%]** during deep recursion.
- *Heuristic Design:* Implemented a **Hamming distance** heuristic combined with depth cost, optimizing the traversal of the decision tree to locate the shortest path in **[Pending: O(b^d) or specific time metric]**.
- *System Architecture:* Designed a robust **OOP** state management system (`Nodo` class) to track parent pointers and movement history, enabling precise solution backtracking and path reconstruction.
- *DevOps & Quality Assurance:* **[Pending: Implemented automated testing pipelines using GitHub Actions to validate algorithm correctness across distinct puzzle configurations]**.

### Deep Chair (2018): Facial Gesture-Driven Wheelchair Control System

- *System Architecture & Integration:* Engineered a decoupled control system bridging Python-based ML inference with C++ embedded firmware (Arduino), managing serial communication protocols to achieve [Pending: XXms] latency for real-time actuation.
- *Deep Learning Pipeline:* Deployed a fine-tuned **ResNet-18** model using **PyTorch**, implementing a custom training loop with **CrossEntropyLoss** and **SGD** optimization to classify 5 distinct gesture states with [Pending: XX%] accuracy.
- *Computer Vision & Data Processing:* Built a video processing pipeline using **OpenCV** and **NumPy** to handle frame extraction, normalization, and augmentation, ensuring robust model performance against environmental variables.
- *Hardware Abstraction:* Developed an auto-detecting hardware interface layer using **PySerial**, creating a fault-tolerant bridge between the vision subsystem and the physical motor drivers.

## Certifications
