import tensorflow as tf
import gradio as gr
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train/255.0
x_test = x_test/255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(64,activation='relu'),
    tf.keras.layers.Dense(32,activation='relu'),
    tf.keras.layers.Dense(16,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adamax', loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])
model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=30)


sketchpad = gr.inputs.Sketchpad()
label = gr.outputs.Label(num_top_classes=3)
gr.Interface(classify, sketchpad, label, live=True, capture_session=True).launch(share=True)
