import tensorflow as tf

x = tf.Variable(2.0)
with tf.GradientTape() as tape:
  y0 = x**2
  y1 = 1 / x
print("Multiple source gradient of different calculation")
print(tape.gradient({'y0': y0, 'y1': y1}, x).numpy())

x = tf.Variable(2.)

with tf.GradientTape() as tape:
  y = x * [3., 4.]
print("Multiple target gradient of the same calculation")
print(tape.gradient(y, x).numpy())

x = tf.linspace(-10.0, 10.0, 200+1)

with tf.GradientTape() as tape:
  tape.watch(x)
  y = tf.nn.sigmoid(x)
print(y)
print(tape.gradient(y, x))

