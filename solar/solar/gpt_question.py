import openai
import requests

from PIL import Image

openai.api_key ="OPEN-AI-API-KEY"


#이미지 생성
def image_create(animal, number):
  # 텍스트 프롬프트를 사용하여 이미지 생성
  response = openai.Image.create(
    prompt=f"{animal} with 8 bit image like old-pokemon style graphic, background color is complement color",
    n=1,
    size="256x256"
  )

  # 생성된 이미지 URL 가져오기
  image_url = response['data'][0]['url']

  image_response = requests.get(image_url)

  # 이미지 파일로 저장
  with open(f'generated_image_{number}.png', "wb") as f:
      f.write(image_response.content)



  input = Image.open(f'generated_image_{number}.png') # load image

  # 입력 이미지 경로 및 출력 이미지 경로
  input_path = f'generated_image_{number}.png'
  output_path = f'generated_image_{number}.png'

  image = Image.open(input_path).convert("RGBA")

  # 제거할 배경 색상 (여기서는 흰색으로 가정, 필요에 따라 변경)
  datas = image.getdata()
  background_color = list(datas[0])[:3]

  # 배경 색상을 투명하게 변경
  new_data = []
  for item in datas:
      color = list(item[:3])
      if ((item[0]-background_color[0])**2+(item[1]-background_color[1])**2+(item[2]-background_color[2])**2)**0.5<50:
          new_data.append((255, 255, 255, 0))  # 완전 투명
      else:
          new_data.append(item)

  # 새로운 이미지 데이터를 적용
  image.putdata(new_data)

  # 결과 이미지를 저장
  image.save(output_path)

  #print(f"Processed image saved as {output_path}")



import openai

# OpenAI API 키 설정
openai.api_key = 'OPEN-AI-API-KEY'

def chat_with_gpt4(messages, model):
    response = openai.ChatCompletion.create(
        model=model,  # 사용할 모델 이름
        messages=messages,
        max_tokens=150,  # 원하는 응답 길이 설정
        n=1,
        stop=None,
        temperature=0.7,  # 응답의 창의성 조절
    )

    reply = response['choices'][0]['message']['content'].strip()
    return reply
#사냥 가능?
def hunt_result(a,b):
  messages = [
      {"role": "system", "content": "You must answer as only 'True' or 'False'"},
      {"role": "user", "content": f"Can {a} hunt {b}?"}
  ]

  reply = chat_with_gpt4(messages, "gpt-3.5-turbo")
  return reply

#어디 사는지
def where_live(a):
  messages = [
      {"role": "system", "content": "You must answer as only one word in {grassland, desert, beach, mountain, polar}. without '.'"},
      {"role": "user", "content": f"what is the best biome {a} to live in (grassland, desert, beach, mountain, polar)?"}
  ]

  reply = chat_with_gpt4(messages, "gpt-3.5-turbo-0125")
  return reply

#주 먹이
def main_diet(a):
  messages = [
      {"role": "system", "content": "You must answer as only one word in {vegetable, meat, fish, fruit}"},
      {"role": "user", "content": f"What is the main diet of {a}?"}
  ]

  reply = chat_with_gpt4(messages, "gpt-3.5-turbo-0301")
  return reply
  
  
#세 특징
def three_characteristic(a):
  messages = [
      {"role": "system", "content": "You must answer only in three sentences form"},
      {"role": "user", "content": f"Describe three characteristic of {a}"}
  ]

  reply = chat_with_gpt4(messages, "gpt-3.5-turbo-0613")
  return reply
  
#성격
def personality():
  messages = [
      {"role": "system", "content": "You must answer as only one word form"},
      {"role": "user", "content": f"Say random one personality"}
  ]

  reply = chat_with_gpt4(messages, "gpt-3.5-turbo-1106")
  return reply
  
#교배
def birth(a,b,region):
  messages = [
      {"role": "system", "content": "You must answer as only one word form. you must not reuse any word in my question"},
      {"role": "user", "content": f"what is the another animal in {region} between {a} and {b}"}
  ]

  reply = chat_with_gpt4(messages, "gpt-3.5-turbo-16k")
  return reply

#품종
def kindof(a,region):
  messages = [
      {"role": "system", "content": "You must answer as only one word form."},
      {"role": "user", "content": f"say random one kind of {a} in {region}"}
  ]

  reply = chat_with_gpt4(messages, "gpt-3.5-turbo-16k-0613")
  return reply

'''
animal1 = 'bear'
animal2 = 'cat'
print(can_hunt(animal1, animal2))
region = where_live(animal1)
print(region)
print(main_diet(animal1))
print(three_characteristic(animal1).split('.'))
print(personality())
new_animal = birth(animal1, animal2, region)
print(new_animal)

kind = kindof(new_animal, region)
kind.replace(new_animal, "")
new_animal = kind + new_animal
print(new_animal)
image_create(new_animal)
'''