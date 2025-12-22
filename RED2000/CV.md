# Adrián Constante

***Backend Developer | DevOps | CloudOps | Data Engineer***

## Contact

- Email: <ad_con.reload@proton.me>
- LinkedIn: <https://linkedin.com/in/adcondev>
- GitHub: <https://github.com/adcondev>

## Professional Summary

DevOps Engineer & Go Developer with a strong foundation in Biomedical Engineering and Computer Science. Expert in architecting high-concurrency backend systems and distributed cloud infrastructure, with a specialized focus on Hardware Abstraction Layers and IoT Integration. Proven track record of engineering production-ready libraries (e.g., "Poster") that decouple complex hardware protocols from business logic, significantly reducing integration latency. Experienced in designing robust CI/CD pipelines, automating cross-platform testing, and managing self-hosted PaaS environments using Docker and Traefik. Adept at bridging the gap between low-level hardware constraints and high-level cloud architectures, delivering scalable solutions for industries ranging from retail POS systems to scientific research at CERN. Passionate about Open Source, Clean Architecture, and Test-Driven Development.

## Technologies and Tools

### Programming Languages

- *Go (Golang):* Primary language for backend, CLIs, and daemons.
- *Python:* Extensive use in API development, data engineering, and ML.
- *SQL:* Schema design and query optimization.
- *C++ / C:* Embedded firmware and legacy hardware integration.
- *Solidity:* Smart contract development.

### Backend Development & Frameworks

- *Go Ecosystem:* Gorilla WebSocket, Templ, Bubbletea (TUI), Go-Serial, HttpRouter.
- *Python Frameworks:* FastAPI, SQLModel, PyVISA.
- *Architecture:* REST APIs, Microservices, WebSocket (Real-time), JSON-RPC.

### DevOps & CI/CD

- *Containerization:* Docker, Docker Compose.
- *CI/CD Automation:* GitHub Actions, Dependabot, Semantic Release, Taskfile.
- *Infrastructure as Code (IaC):* Terraform, Ansible.
- *Orchestration & PaaS:* Dokploy, Traefik (Reverse Proxy/Load Balancer).

### Cloud Infrastructure & Platforms

- *Providers:* DigitalOcean (Droplets/VPS), AWS (EC2).
- *Networking:* SSL Termination, Reverse Proxies, UFW (Firewall).
- *Monitoring & Tooling:* Postman, n8n.

### Data Engineering & Databases

- *Databases:* PostgreSQL, MySQL, Dynamics 365.
- *Big Data & ETL:* PySpark, Databricks, Pandas, NumPy.
- *Data Serialization:* JSON Schema, Protocol Buffers (implied by gRPC contexts/struct mapping).

### Embedded Systems & Low-Level

- *Hardware Interface:* FPGA (Xilinx), CUDA, Tensor Cores.
- *IoT & Protocols:* RS232/Serial Communication, ESC/POS (Thermal Printing), Arduino.
- *System Programming:* Windows Services, Syscall/Unsafe (Go), Memory Management.

### Machine Learning & AI

- *Frameworks:* PyTorch, OpenCV, Scikit-learn (implied by ML coursework).
- *Applications:* LLM Fine-tuning (RLHF), Computer Vision (Mask-RCNN), LSTM Networks, NLP.
- *Concepts:* Backpropagation, Gradient Descent, Vectorization.

### Software Architecture & Design

- *Patterns:* Clean Architecture, Dependency Injection, Facade Pattern, Interface-Driven Design.
- *Methodologies:* Test-Driven Development (TDD), 12-Factor App.
- *Algorithms:* A* Search, Huffman Coding, Bloom Filters, Dithering (Floyd-Steinberg/Atkinson).

### Security & Cryptography

- *Auth & Identity:* OAuth2, JWT, RBAC (Role-Based Access Control).
- *Security Tools:* CodeQL (Static Analysis), Bcrypt.
- *Cryptographic Protocols:* RSA, HMAC, SHA-1, Blockchain (Ethereum).

### Web Technologies (Frontend Support)

- *Libraries:* Alpine.js, Angular, Web3.js.
- *Tools:* HTML/CSS Templates, Chrome DevTools (implied by debugging).

## Experience

### Go Developer | RED 2000

Mazatlán, Mexico | 2025/06 - Present

- Architected a production-ready Go library ("Poster") for thermal printers, utilizing pattern principles to decouple protocol logic from hardware drivers.
- Developed a custom JSON-to-ESC/POS translation engine, creating a structured schema validator and command builder to convert complex JSON payloads (including QR codes and Tables) into hardware-specific byte streams.
- Optimized system concurrency using Go primitives to implement printing queues with buffered channels, effectively handling backpressure and race conditions during concurrent device access.
- Designed a WebSocket-based Daemon service to enable real-time, bidirectional communication between web clients and physical hardware (scales, printers), replacing legacy constructor-based logic with a flexible JSON command architecture.
- Engineered comprehensive CI/CD pipelines using GitHub Actions, automating cross-platform testing (Windows, Linux, macOS), semantic releases, and dependency management via Dependabot to ensure code stability.
- Orchestrated a self-hosted PaaS infrastructure on a DigitalOcean VPS using Docker Compose and Traefik as a reverse proxy/load balancer, managing containerized microservices with SSL termination.
- Enforced code security and quality by integrating CodeQL for static analysis and vulnerability scanning, alongside automated linter workflows to maintain strict coding standards.
- Implemented robust testing strategies including Dependency Injection, Mocking, and Table-driven tests, achieving high reliability by simulating hardware states without physical dependencies.
- Engineered an image processing engine for hardware constraints, implementing dithering algorithms and base64 decoding pipelines to optimize high-resolution graphics for low-memory thermal printing devices.

### TI Instructor and Developer | Hackerson IT

Mazatlán, Mexico | 2025/01 - Now

- Delivered advanced technical training in Python and Web Development to pre-university students, guiding them from algorithmic logic to building functional applications.
- Led robotics and automation workshops for the Mapletree Academy partnership, introducing engineering fundamentals through Lego programming and sensor logic integration.
- Mentored students through the full software development lifecycle in hands-on projects (Game Dev, Chatbots), emphasizing code logic, debugging, and creative implementation.
- Collaborated with educational stakeholders to deploy a technology specialization program, standardizing the teaching of robotics and programming logic.

### RHLF Trainer | Outlier

Mazatlán, Mexico | 2023/06 - Now

- Engineered high-quality training data for LLM fine-tuning (RLHF), rigorously auditing Go and Python code generation to minimize hallucinations and ensure syntax correctness.
- Evaluated model performance across complex engineering tasks —including debugging, refactoring, and algorithmic implementation—providing critical feedback to improve the model's reasoning and problem-solving logic.
- Authored detailed "Chain of Thought" justifications, training the model to prioritize idiomatic code practices, efficient time complexity, and robust error handling in backend scenarios.

### Independent & Personal Projects | AdConDev

Mazatlán, Mexico | 2023/06 - 2025/01

- Architected and deployed full-stack web solutions using the Go ecosystem (including Templ for server-side rendering) and Alpine.js, delivering high-performance, lightweight applications for private clients.
- Managed self-hosted infrastructure on Linux VPS environments, utilizing Dokploy to orchestrate containerized deployments (Docker) and reverse proxies, effectively replacing costly managed PaaS alternatives.
- Expanded Python and Data Engineering expertise, developing high-performance REST APIs with FastAPI and SQLModel, while deepening knowledge of distributed computing architecture using PySpark and Databricks.
- Established robust CI/CD pipelines via GitHub Actions, automating Unit Testing (Go) and API verification (Postman) to ensure production reliability for freelance deliverables.

### Backend Developer - Dynamics 365 | Havox IT

Mexico City, Mexico | 2022/01 - 2023/06

- Customized Dynamics 365 data architecture, extending table schemas and configuring entity relationships to enhance UI functionality and streamline user workflows.
- Optimized backend performance by engineering efficient SQL views and queries, significantly reducing load times for data retrieval and Power BI reporting integrations.
- Bridged the gap between technical and financial teams, translating complex database schemas and relationship logic to facilitate accurate data analysis by non-technical stakeholders.

### Research Assistant | CERN

Geneva, Switzerland | 2018/10 - 2018/12

- Engineered automated data acquisition pipelines using Python and PyVISA to orchestrate high-end instrumentation (oscilloscopes), enabling unattended overnight testing of photomultiplier components.
- Collaborated with experimental physicists to design and validate measurement protocols for next-generation ion collision sensors within the ALICE experiment framework.

## Education

### MSc. Computer Science (Truncated) | CINVESTAV Guadalajara | Guadalajara, Mexico

- Master's Thesis: "Hardware Module for LSTM Gates Acceleration".
- Designed an FPGA hardware module to accelerate training and inference for LSTM recurrent neural networks, focusing on NLP and sentiment analysis optimization.
- Optimized parallel processing of LSTM gates utilizing CUDA, GPU architecture, and Tensor Cores, significantly improving computational efficiency for deep learning models.
- Key Coursework: Distributed Systems, High Performance Computing (HPC), Cryptography, Computer Networks, Graph Theory, Data Structures & Algorithms, Machine Learning.

### BE. Biomedical Engineering | Universidad Politécnica de Sinaloa | Sinaloa, Mexico

- Activities: Combined applied Machine Learning with medical image and time-series analysis.
- Developed end-to-end instrumentation solutions involving digital/analog sensing and signal processing.
- Key Coursework: Object-Oriented Programming (OOP), Databases, Digital Signal Processing (DSP), Time-series Data Analysis, IoT Devices, Statistical Data Analysis.

## Major Projects

### Poster: High-Performance Thermal Printer Driver & Protocol Engine (2025)

- System Architecture: Architected a modular Go (1.24+) library utilizing Interface-Driven Design and Facade Patterns to decouple business logic from hardware protocols.
- Designed a versioned JSON Schema middleware that validates and transforms structured data into binary ESC/POS commands, reducing client integration time by [Pending: Estimate % or Hours Saved].
- Low-Level Engineering: Engineered a custom Windows Print Spooler integration using syscall and unsafe to manage kernel-level print jobs.
- Implemented a complex C-struct mapping strategy to bypass standard driver buffering, reducing print-start latency by [Pending: Estimate %] compared to legacy drivers.
- Algorithm Design: Developed a dependency-free Graphics Engine implementing Atkinson Dithering and Bilinear Interpolation to optimize image rendering for 1-bit thermal heads.
- Created a Dynamic Table Engine utilizing a "reduce longest first" algorithm that mathematically ensures data fits within physical paper margins.
- DevOps & Quality Assurance: Established a Tier-1 CI/CD Pipeline using GitHub Actions, automating Semantic Versioning and cross-platform builds.
- Designed a Visual Emulator that renders print jobs as PNGs, enabling Test-Driven Development (TDD) and automated regression testing without physical devices.
- Protocol Engineering: Implemented a Hybrid Execution Strategy that intelligently switches between native firmware commands and software-based rasterization (for QR/Barcodes) based on a dynamically loaded device profile, ensuring 100% compatibility across generic hardware.

### Automated Cloud Infrastructure: Local-to-Production Pipeline (2025)

- *Infrastructure as Code (IaC) & Orchestration:* Architected a reproducible local-to-production pipeline using Terraform and Ansible for cloud provisioning (DigitalOcean), paired with a Docker Compose environment that simulates production locally; this standardization reduced server configuration time by [Pending: XX%].
- *Self-Hosted PaaS & Networking:* Engineered a secure platform using Dokploy and Traefik for automated SSL termination in production, while utilizing ngrok and private bridge networks locally to expose isolated services to public webhooks during development.
- *Data Engineering & Automation:* Deployed a high-performance n8n stack backed by PostgreSQL (Production) and persistent volumes (Local), ensuring data integrity for [Pending: Number] daily workflows involving complex API integrations (Stripe, Slack) and local LLM inference (Ollama).
- *Security Architecture:* Implemented a "Defense in Depth" strategy adhering to 12-Factor App standards, utilizing UFW, isolated Docker networks, and .env secret management to secure both local API keys and production cross-service communication.
- *Operational Impact:* Replaced managed cloud services with this bespoke solution, resulting in an estimated [Pending: xx%] reduction in monthly costs and [Pending: %] faster development cycles by eliminating the need for paid cloud VPS instances during testing.

### Printer Daemon: Go WebSocket Middleware for POS Hardware (2025)

- *System Architecture:* Architected a concurrent **WebSocket server** in **Go (1.24+)** using `gorilla/websocket`, implementing thread-safe connection management (Mutex/Channels) to enable bidirectional communication between web clients and local hardware.
- *Hardware Optimization:* Engineered a custom **Hardware Abstraction Layer (HAL)** for ESC/POS protocols, developing a "Force Flush" algorithm to bypass Windows Print Spooler buffering, reducing print start latency by **[Pending: XX%]**.
- *Dynamic Templating:* Designed a **JSON-driven layout engine** that decouples business logic from rendering, allowing automatic content adaptation for distinct paper widths (58mm/80mm) and reducing client configuration time by **[Pending: XX%]**.
- *DevOps & Tooling:* Standardized the build and release lifecycle using **Taskfile**, automating binary compilation and unit testing to ensure consistent deployment across **[Pending: Number]** Windows terminals.

### Scale Daemon: Industrial IoT Middleware & Windows Service (2025)

- *System Engineering:* Architected a decoupled **Windows Service** in **Go (1.24+)** to bridge industrial scales (RS232) with web clients, utilizing **WebSockets** and Go concurrency primitives (Channels, Mutex) to achieve **[Pending: XXms]** real-time data latency.
- *Resilience & Reliability:* Implemented a fault-tolerant serial communication layer using `go-serial`, featuring automatic reconnection and noise filtering to ensure **[Pending: 99.X%]** uptime in unstable hardware environments.
- *DevOps & Tooling:* Engineered a self-contained distribution pipeline using **Taskfile**, resulting in a custom **TUI Installer** (Bubbletea) that reduces on-site deployment time by **[Pending: XX%]** through automated service lifecycle management.
- *Configuration Management:* Designed a thread-safe hot-reload mechanism allowing dynamic switching of hardware drivers and ports without service interruption, facilitating support for **[Pending: Number of brands/models]** distinct scale manufacturers.

### POS Daemon: Go Middleware for Thermal Printing (2025)

- *System Architecture:* Architected a protocol-agnostic middleware in **Go (1.24+)** using interface-driven design, decoupling business logic from hardware constraints to support multiple printer profiles (58mm/80mm) and protocols (ESC/POS).
- *Hardware Integration:* Engineered a custom **Hardware Abstraction Layer (HAL)** and **Windows Print Spooler** connector, ensuring reliable job queuing and reducing print failures by **[Pending: XX%]** through robust error handling.
- *Algorithm Engineering:* Implemented **Floyd-Steinberg dithering** algorithms to optimize bitmap rendering for 1-bit thermal heads, enabling high-fidelity logo printing with **[Pending: minimal/low]** memory overhead.
- *Template Engine:* Designed a **JSON-driven template system** to generate dynamic receipts, separating layout from logic; this reduced client customization time by **[Pending: XX%]** by eliminating the need for recompilation.
- *DevOps & CI/CD:* Established automated build and test pipelines using **GitHub Actions**, validating code stability across **[Pending: Number]** distinct environments/configurations prior to release.

### Snippet Box: Secure Code Repository and Web Server (2024)

- *Backend Engineering:* Architected a secure, self-hosted web application using *Go (v1.22+)* and *MySQL*, utilizing `httprouter` and custom middleware for observability and security (CSRF protection, TLS 1.3, bcrypt hashing).
- *DevOps & Automation:* Established a DevOps workflow using *GitHub Actions* for CI/CD automation and *Taskfile* for build scripting. Containerized application using *Docker/Docker Compose* for consistent environments.
- *Infrastructure & Deployment:* Deployed application to *DigitalOcean Droplets* behind a *Traefik* reverse proxy, ensuring 99.9% uptime and sub-100ms response times for personal data management.
- *Database Management:* Designed a normalized MySQL schema with optimized indexing for efficient data retrieval, handling [Pending: X number of records/transactions].

### Yalemi API: Scalable Social Media Backend (2023)

- *Backend Architecture:* Architected a high-performance REST API using **FastAPI** and **Python 3.10+**, implementing asynchronous I/O to handle **[Pending: X request volume or concurrent users]** with minimal latency.
- *Data Engineering:* Designed a normalized **PostgreSQL** schema using **SQLModel**, optimizing complex SQL queries (Joins/Selects) to achieve **[Pending: XXms]** query performance for voting and content retrieval.
- *Security & Auth:* Implemented a production-grade **OAuth2** authentication system with **JWT** and **Bcrypt** hashing, ensuring stateless and secure session management for user data.
- *DevOps & CI/CD:* Engineered an automated release pipeline using **GitHub Actions**, managing **Semantic Versioning** and changelogs to streamline the deployment lifecycle across **[Pending: Number of releases/commits]**.

### Low-Level LSTM and FPGA Bridge: Recurrent Neural Network Implementation (2022)

- *Algorithm Engineering:* Engineered a dependency-free **LSTM Neural Network** in **Python** and **NumPy**, manually implementing **Backpropagation Through Time (BPTT)** and the **Adam Optimizer** to achieve **[Pending: XX%]** accuracy in character-level text generation.
- *Data Engineering:* Built a robust ETL pipeline using **Pandas** to process **[Pending: Number of Records]** raw text entries, handling one-hot encoding and sequence padding to optimize matrix vectorization and training throughput.
- *Hardware Deployment:* Architected a model serialization layer to export trained weights as **.coe (Coefficient)** files, facilitating the deployment of software-trained models onto **Xilinx FPGA** block memory for hardware acceleration.
- *Performance Optimization:* Implemented vectorized matrix operations for LSTM gating mechanisms (Forget, Input, Output), reducing computational overhead by **[Pending: XX%]** compared to iterative loop approaches.

### Py-Neumann: Von Neumann Architecture Simulator (2021)

- *System Architecture:* Architected a modular simulation of computer hardware using **Python 3** and **OOP** (Multiple Inheritance), decoupling CPU, Memory, and I/O logic to accurately model the **Fetch-Decode-Execute** cycle.
- *Data Engineering:* Implemented efficient memory state management using **NumPy** for grid manipulation and **Pandas** for structured debugging logs, visualizing 100 memory addresses and register states in real-time.
- *Interpreter Design:* Developed a custom machine code interpreter and file parser to execute distinct opcodes (Arithmetic, Control Flow, Data Movement), translating raw text input into executable CPU instructions.
- *DevOps & Quality Assurance:* [Pending: Implemented automated testing/linting pipelines using GitHub Actions to ensure logic correctness across CPU cycles].
- *Distribution:* [Pending: Containerized application logic or created standalone executables to facilitate cross-platform educational deployment].

### Physio-Key-Gen: Biometric Cryptographic Protocol (2020)

- *Algorithm Engineering:* Engineered a custom **Bloom Filter** implementation in **Python 3** using `bitarray`, optimizing set reconciliation for distributed sensor nodes with a targeted **[Pending: 0.XX%]** false positive rate.
- *Data Pipeline:* Architected a signal processing pipeline using **NumPy** and **WFDB** to extract Inter-Pulse Intervals (IPI) from the MIT-BIH Arrhythmia Database, processing records with **[Pending: XXms]** latency.
- *Security Protocol:* Designed a challenge-response authentication flow utilizing **HMAC** and **SHA-1**, enabling secure key agreement without transmitting raw biometric data across the network.
- *Simulation & Modeling:* Developed a simulation environment to validate protocol robustness against noise, demonstrating successful key establishment in **[Pending: XX%]** of test cases.

### Huffman Cipher: Hybrid Cryptography & Compression Engine (2020)

- *Algorithm Engineering:* Architected a hybrid **"Compress-then-Encrypt"** pipeline in **Python 3**, integrating **Huffman Coding** with a custom **RSA** implementation to achieve **[Pending: XX%]** reduction in message size prior to encryption.
- *Low-Level Implementation:* Engineered cryptographic primitives from first principles (excluding external crypto libraries), implementing **Modular Exponentiation** and the **Extended Euclidean Algorithm** to manage public/private key derivation.
- *Data Structures:* Developed custom **Priority Queues** and **Binary Trees** to handle frequency analysis and bitstream serialization, optimizing the conversion of variable-length codes into fixed encryption blocks.
- *Data Analysis:* Designed an information-theoretic analysis module to calculate **Shannon Entropy** and **Redundancy**, validating compression performance against theoretical limits for datasets up to **[Pending: File Size/Line Count]**.
- *Code Quality & DevOps:* Implemented a modular **OOP** architecture for logic encapsulation and established **[Pending: Unit Tests/CI Pipeline]** to validate the integrity of bitwise operations and mathematical correctness.

### Cliniva: Decentralized Electronic Health Record System (2020)

- *Distributed Systems Architecture:* Architected a hybrid storage solution utilizing **Ethereum** for immutable metadata and **IPFS** for decentralized content, reducing on-chain storage costs by **[Pending: XX%]** via hash-pointer referencing.
- *Smart Contract Engineering:* Developed modular **Solidity** contracts with **Role-Based Access Control (RBAC)** and **OpenZeppelin** standards, implementing a "Circuit Breaker" pattern to ensure system security during critical failures.
- *Full-Stack Integration:* Bridged **Angular** frontend interfaces with the **EVM** using **Web3.js**, managing transaction signing and asynchronous state synchronization for **[Pending: Number of Users/Records]**.
- *DevOps & Testing:* Managed the smart contract lifecycle using **Truffle Suite** and **Ganache** for local simulation, executing automated migration scripts and unit tests to ensure logical correctness prior to deployment.

### Matrix Petri Net Simulator: Discrete Event System Engine (2020)

- *Algorithm Engineering:* Architected a matrix-based simulation engine in **Python 3**, translating formal mathematical tuples $(P, T, Pre, Post, M_0)$ into an executable **Object-Oriented** system to model concurrent processes.
- *Data Engineering & Optimization:* Implemented **vectorized state transitions** using **NumPy**, utilizing Pre/Post-incidence matrices to replace nested loops; this optimized the "firing rule" calculation logic by **[Pending: XX%]** compared to iterative approaches.
- *System Architecture:* Designed a robust **Command Line Interface (CLI)** and continuous simulation loop that dynamically identifies enabled transitions and performs automatic **deadlock detection** to ensure system stability.
- *DevOps & Quality Assurance:* **[Pending: Established automated testing pipelines using GitHub Actions to validate matrix logic and transition integrity across distinct network topologies].**

### A* 8-Puzzle Solver: Heuristic Search Engine (2019)

- *Algorithm Engineering:* Engineered a dependency-free **A* (A-Star)** search algorithm in **Python 3**, implementing the `f(n) = g(n) + h(n)` cost function to solve optimization problems with **[Pending: XX%]** greater efficiency than non-heuristic methods (BFS/DFS).
- *Data Structures:* Architected a custom **Priority Queue** (`BestFirst`) and **Hash-based Closed Set** (`ColaQ`) to manage state space, implementing cycle detection to reduce memory overhead by **[Pending: XX%]** during deep recursion.
- *Heuristic Design:* Implemented a **Hamming distance** heuristic combined with depth cost, optimizing the traversal of the decision tree to locate the shortest path in **[Pending: O(b^d) or specific time metric]**.
- *System Architecture:* Designed a robust **OOP** state management system (`Nodo` class) to track parent pointers and movement history, enabling precise solution backtracking and path reconstruction.
- *DevOps & Quality Assurance:* **[Pending: Implemented automated testing pipelines using GitHub Actions to validate algorithm correctness across distinct puzzle configurations]**.

### Deep Chair: Facial Gesture-Driven Wheelchair Control System (2018)

- *System Architecture & Integration:* Engineered a decoupled control system bridging Python-based ML inference with C++ embedded firmware (Arduino), managing serial communication protocols to achieve [Pending: XXms] latency for real-time actuation.
- *Deep Learning Pipeline:* Deployed a fine-tuned **ResNet-18** model using **PyTorch**, implementing a custom training loop with **CrossEntropyLoss** and **SGD** optimization to classify 5 distinct gesture states with [Pending: XX%] accuracy.
- *Computer Vision & Data Processing:* Built a video processing pipeline using **OpenCV** and **NumPy** to handle frame extraction, normalization, and augmentation, ensuring robust model performance against environmental variables.
- *Hardware Abstraction:* Developed an auto-detecting hardware interface layer using **PySerial**, creating a fault-tolerant bridge between the vision subsystem and the physical motor drivers.

### Seahawk: Security for Mazatlan’s beaches (2018)

- Developed a drone computer vision system using Mask-RCNN to detect swimmers at risk in the ocean.
- Spearheaded the image processing component, segmenting video feeds into beach, sea, and people in OpenCV, with a model trained on a AWS EC2 GPU instance.
- We won a hackathon with it.

## Certifications

[Worth mention any related certification as being pursued]
