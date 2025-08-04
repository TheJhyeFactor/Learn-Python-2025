# Module 07: Network Programming

## 🎯 Learning Objectives
- Create TCP/IP connections with sockets
- Implement client-server communication
- Perform port scanning
- Extract service banners
- Handle network errors gracefully

## 🛡️ Why it matters for a pentester
Network programming is the core of reconnaissance. Whether you're mapping services, grabbing banners, or testing for vulnerabilities, sockets give you low-level control over network interactions.

## 📚 Vocabulary
- **Socket**: Endpoint for network communication
- **TCP**: Reliable, connection-oriented protocol
- **Port**: Logical connection point (1-65535)
- **Banner**: Service identification string
- **Three-way handshake**: TCP connection establishment
- **Bind**: Associate socket with address/port
- **Listen**: Wait for incoming connections

## 📂 Example References
- `lanspy.py` - Basic hostname and IP resolution
- `socket_testing.py` - Ping sweep and network discovery
- `LanSpy_Project_Overview.md` - Complete project requirements

## 💡 Mini-Project: TCP Port Scanner
Build a scanner that:
- Takes target IP and port range
- Attempts TCP connection to each port
- Grabs banners from open ports
- Outputs clean results with service detection
- Handles timeouts and refused connections

## ✅ Checkpoint Questions
1. What's the difference between `connect()` and `connect_ex()`?
2. Why use timeout values with sockets?
3. How do you handle "Connection refused" vs "Host unreachable"?

## 🔗 Prerequisites
- Module 06B: Subprocess (for system commands)
- Module 04: Exception handling (for network errors)

## 🔗 Next Steps
Ready to verify your code works? Move to Module 08: Testing & Debugging