# Luke Hart
# Handwitten Digit Recognition
# Basically the same, but now I actually have to do stuff
# Hopefully I learned something from the last one
# is this supposed to be awful? Or am i missing something?

import tensorflow as tf     # get'n muh tools

from tensorflow.examples.tutorials.mnist import input_data      # getting
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)  # muh data

hidden_layer_size = 500
input_size = 784
class_size = 10

x = tf.placeholder(tf.float32, [None, input_size]) # input placeholder

hidden_Weights = tf.Variable(tf.random_normal([input_size, hidden_layer_size]))
hidden_Biases = tf.Variable(tf.random_normal([hidden_layer_size]))
W = tf.Variable(tf.random_normal([hidden_layer_size, class_size]))        # Output Weights
b = tf.Variable(tf.random_normal([class_size]))                           # Out Bias

hidden_layer = tf.matmul(x, hidden_Weights) + hidden_Biases
hidden_layer = tf.nn.sigmoid(hidden_layer)


y = tf.matmul(hidden_layer, W) + b                     # output, like this because apparently logits are really good or something

y_ = tf.placeholder(tf.float32, [None, class_size])     # Correct answer input placeholder

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
                                        # Apparently better than
# cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
                                        # What we'll be using to train the model

sess = tf.InteractiveSession()          # creates a thing to run the model in

tf.global_variables_initializer().run() # Makes all the variables real, apparently

for _ in range(1000):                   # Train 1000 times
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))  # Test the model
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) # compute accuracy
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})) # Print accuracy
