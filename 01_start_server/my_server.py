from fastmcp import FastMCP

mcp = FastMCP("我的 MCP 服务器")

@mcp.tool
def greet(name: str) -> str:
    return f"你好，{name}！"

if __name__ == "__main__":
    # stdio 传输是将 MCP 服务器连接到客户端的传统方式
    # mcp.run()
    # http 传输是将 MCP 运行在 HTTP 服务器上的方式
    mcp.run(transport="http", port=8000)
