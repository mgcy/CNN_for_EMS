"""4-Layer Convolutional Neural Network Estimator for MNIST, built with tf.layers."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

import datetime as dt

tf.logging.set_verbosity(tf.logging.INFO)


def cnn_model_fn(features, labels, mode):
    """Model function for CNN."""
    # Input Layer
    # Reshape X to 4-D tensor: [batch_size, width, height, channels]
    # MNIST images are 28x28 pixels, and have one color channel
    input_layer = tf.reshape(features["x"], [-1, 90, 90, 1])

    # Convolutional Layer #1
    # Computes 32 features using a 5x5 filter with ReLU activation.
    # Padding is added to preserve width and height.
    # Input Tensor Shape: [batch_size, 90, 90, 1]
    # Output Tensor Shape: [batch_size, 80, 80, 32]
    conv1 = tf.layers.conv2d(
        inputs=input_layer,
        filters=32,
        kernel_size=[11, 11],
        padding="valid",
        activation=tf.nn.relu)

    # Pooling Layer #1
    # First max pooling layer with a 2x2 filter and stride of 2
    # Input Tensor Shape: [batch_size, 80, 80, 32]
    # Output Tensor Shape: [batch_size, 40, 40, 32]
    pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)

    # Convolutional Layer #2
    # Computes 64 features using a 5x5 filter.
    # Padding is added to preserve width and height.
    # Input Tensor Shape: [batch_size, 40, 40, 32]
    # Output Tensor Shape: [batch_size, 32, 32, 64]
    conv2 = tf.layers.conv2d(
        inputs=pool1,
        filters=64,
        kernel_size=[9, 9],
        padding="valid",
        activation=tf.nn.relu)

    # Pooling Layer #2
    # Second max pooling layer with a 2x2 filter and stride of 2
    # Input Tensor Shape: [batch_size, 32, 32, 64]
    # Output Tensor Shape: [batch_size, 16, 16, 64]
    pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)

    # Convolutional Layer #3
    # Computes 32 features using a 5x5 filter with ReLU activation.
    # Padding is added to preserve width and height.
    # Input Tensor Shape: [batch_size, 16, 16, 64]
    # Output Tensor Shape: [batch_size, 8, 8, 128]
    conv3 = tf.layers.conv2d(
        inputs=pool2,
        filters=128,
        kernel_size=[9, 9],
        padding="valid",
        activation=tf.nn.relu)

    # Pooling Layer #3
    # First max pooling layer with a 2x2 filter and stride of 2
    # Input Tensor Shape: [batch_size, 8, 8, 128]
    # Output Tensor Shape: [batch_size, 4, 4, 128]
    pool3 = tf.layers.max_pooling2d(inputs=conv3, pool_size=[2, 2], strides=2)

    # Flatten tensor into a batch of vectors
    # Input Tensor Shape: [batch_size, 6, 7, 64]
    # Output Tensor Shape: [batch_size, 6 * 7 * 64]
    # pool3_flat = tf.reshape(pool3, [-1, 2 * 2 * 128])
    pool3_flat = tf.reshape(pool3, [-1, 4 * 4 * 128])
    # Logits layer
    # Output Tensor Shape: [batch_size, 4]
    logits = tf.layers.dense(inputs=pool3_flat, units=4)

    predictions = {
        # Generate predictions (for PREDICT and EVAL mode)
        "classes": tf.argmax(input=logits, axis=1),
        # Add `softmax_tensor` to the graph. It is used for PREDICT and by the
        # `logging_hook`.
        "probabilities": tf.nn.softmax(logits, name="softmax_tensor")
    }
    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)

    # Calculate Loss (for both TRAIN and EVAL modes)
    loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

    # Configure the Training Op (for TRAIN mode)
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.AdamOptimizer(learning_rate=0.00001)
        train_op = optimizer.minimize(
            loss=loss,
            global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)

    # Add evaluation metrics (for EVAL mode)
    eval_metric_ops = {
        "accuracy": tf.metrics.accuracy(
            labels=labels, predictions=predictions["classes"])}
    return tf.estimator.EstimatorSpec(
        mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


def main(unused_argv):
    # monitor start time
    start_time = dt.datetime.now()
    print('Start learning at {}'.format(str(start_time)))

    # Load training and eval data, returns np.array
    train_data = np.loadtxt('D:\Academic\data_nvspl\\SRCID_LAKE017_data_training_SC.txt', dtype="float32")
    train_labels = np.loadtxt('D:\Academic\data_nvspl\SC_Q\\label_training_90_pure_silence.txt', dtype="int32")
    eval_data = np.loadtxt('D:\Academic\data_nvspl\\SRCID_LAKE017_data_testing_SC.txt', dtype="float32")
    eval_labels = np.loadtxt('D:\Academic\data_nvspl\SC_Q\\label_testing_90_pure_silence.txt', dtype="int32")

    # gaussian_image = gaussian(original_image, 20, 20)

    print("Load data successfully")

    # Create the Estimator
    mnist_classifier = tf.estimator.Estimator(
        model_fn=cnn_model_fn, model_dir="/tmp/nvspl_cnn_adam_90_8_pure_sil_SC_post_3layers_model")

    # Set up logging for predictions
    # Log the values in the "Softmax" tensor with label "probabilities"
    tensors_to_log = {"probabilities": "softmax_tensor"}
    logging_hook = tf.train.LoggingTensorHook(
        tensors=tensors_to_log, every_n_iter=50)
    # f1 = open("D:\Academic\data_nvspl\\SRCID_LAKE017_delete.txt", 'w')
    for i_train in range(5):
        # Train the model
        train_input_fn = tf.estimator.inputs.numpy_input_fn(
            x={"x": train_data},
            y=train_labels,
            batch_size=100,
            num_epochs=None,
            shuffle=True)
        mnist_classifier.train(
            input_fn=train_input_fn,
            steps=500,
            hooks=[logging_hook])

        # Evaluate the model
        eval_input_fn = tf.estimator.inputs.numpy_input_fn(
            x={"x": eval_data},
            y=eval_labels,
            num_epochs=1,
            shuffle=False)

        # Predict output
        predictions = mnist_classifier.predict(input_fn=eval_input_fn)
        output_labels = []
        for p in predictions:
            output_labels.append(p['classes'])

        # Print results
        eval_results = mnist_classifier.evaluate(input_fn=eval_input_fn)
        print(eval_results)
        # f1.write(eval_results + '\n')

        # Confusion matrix
        conf = tf.confusion_matrix(
            labels=eval_labels,
            predictions=output_labels,
            num_classes=4,
            dtype=tf.int32,
            name=None,
            weights=None
        )
        sess = tf.InteractiveSession()
        sess.run(tf.global_variables_initializer())

        confusion_matrix = sess.run(conf)
        print(confusion_matrix)
        # f1.write(confusion_matrix + '\n')
    # f1.close()

    # monitor end time
    end_time = dt.datetime.now()
    print('Stop learning {}'.format(str(end_time)))
    elapsed_time = end_time - start_time
    print('Elapsed learning {}'.format(str(elapsed_time)))


if __name__ == "__main__":
    tf.app.run()
