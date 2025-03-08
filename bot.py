import discord
from discord import app_commands
import random

# 봇 인텐트 설정
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# 랜덤 응답 메시지 목록
HELLO_RESPONSES = [
    "안녕하세요! 반가워요.",
    "Hello there!",
    "반갑습니다~",
    "오늘도 좋은 하루 되세요!",
    "어서오세요! 무엇을 도와드릴까요?",
    "안녕! 기분이 어때요?",
    "방문해주셔서 감사합니다!"
]

# 봇이 준비되었을 때 실행되는 이벤트
@client.event
async def on_ready():
    print(f'봇이 {client.user}로 로그인했습니다')
    await tree.sync()  # 명령어 동기화

# /hello 명령어 정의
@tree.command(name="hello", description="인사말을 랜덤으로 출력합니다")
async def hello(interaction: discord.Interaction):
    # 랜덤한 응답 선택
    response = random.choice(HELLO_RESPONSES)
    await interaction.response.send_message(response)

# 봇 실행
# 아래 YOUR_BOT_TOKEN 부분에 디스코드 봇 토큰을 입력하세요
client.run(DISCORD_TOKEN)
