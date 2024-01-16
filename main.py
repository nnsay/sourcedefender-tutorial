import requests


def get_github_status():
    # GitHub Status API endpoint
    api_url = "https://www.githubstatus.com/api/v2/status.json"

    try:
        # 发送 GET 请求获取 GitHub 当前状态信息
        response = requests.get(api_url)

        # 检查请求是否成功
        if response.status_code == 200:
            # 解析 JSON 响应
            status_data = response.json()

            # 提取状态信息
            status = status_data.get("status")
            description = status_data.get("body", {}).get("markdown")

            # 打印状态信息
            print(f"GitHub Status: {status}")
            print(f"Status Description: {description}")

        else:
            print(
                f"Failed to retrieve GitHub status. Status code: {response.status_code}"
            )

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_github_status()
