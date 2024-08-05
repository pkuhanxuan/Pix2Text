from pix2text import Pix2Text
import psutil
import GPUtil
import time

def print_resource_usage():
	# 获取CPU和内存使用情况
	cpu_usage = psutil.cpu_percent(interval=1)
	memory_info = psutil.virtual_memory()
	memory_usage = memory_info.percent
	
	# 获取GPU使用情况
	gpus = GPUtil.getGPUs()
	gpu_usage = [(gpu.id, gpu.load * 100, gpu.memoryUtil * 100) for gpu in gpus]
	
	print(f"CPU使用率: {cpu_usage}%")
	print(f"内存使用率: {memory_usage}%")
	for gpu_id, gpu_load, gpu_memory in gpu_usage:
		print(f"GPU {gpu_id} 使用率: {gpu_load}%, 内存使用率: {gpu_memory}%")

img_fp = './流体力学 (光坰·周) (z-lib.org)_35-100.pdf'
p2t = Pix2Text.from_config()
print('加载模型完成')
print_resource_usage()
doc = p2t.recognize_pdf(img_fp, page_numbers=[0, 65])
print('识别完成')
print_resource_usage()
doc.to_markdown('output-md')  # 导出的 Markdown 信息保存在 output-md 目录中
print('导出完成')
print_resource_usage()
