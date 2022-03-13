import os

walks = list(os.walk(r'F:\Archived Download\first-order-motion-model-20200616T103033Z-001\first-order-motion-model'))
for walk in walks:
    print(walk)