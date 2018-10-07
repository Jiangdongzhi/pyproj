import paddle.v2 as paddle

lists = []
def softmax_regression(img):
    predict = paddle.layer.fc(input=img,
                              size=10,
                              act=paddle.activation.Softmax())
    return predict

def event_handler(event):
    if isinstance(event, paddle.event.EndIteration):
        if event.batch_id % 100 == 0:
            print "Pass %d, Batch %d, Cost %f, %s" % (event.pass_id, event.batch_id, event.cost, event.metrics)
    if isinstance(event, paddle.event.EndPass):
        with open('params_pass_%d.tar' % event.pass_id, 'w') as f:
            trainer.save_parameter_to_tar(f)

        result = trainer.test(reader=paddle.batch(paddle.dataset.mnist.test(), batch_size=128))
        print "Test with Pass %d, Cost %f, %s\n" % (event.pass_id, result.cost, result.metrics)

paddle.init(use_gpu=False, trainer_count=1)

images = paddle.layer.data(name="pixel", type=paddle.data_type.dense_vector(784))

label = paddle.layer.data(name="label", type=paddle.data_type.integer_value(10))

predict = softmax_regression(images)
#predict = multilayer_perceptron(images)
#predict = dnn(images)

cost = paddle.layer.classification_cost(input=predict, label=label)