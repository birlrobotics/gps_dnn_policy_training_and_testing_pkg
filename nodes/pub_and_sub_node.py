#!/usr/bin/env python
import rospy
from gps_dnn_policy_training_and_testing_pkg.CONSTANT import training_request_topic, training_response_topic
from gps_dnn_policy_training_and_testing_pkg.dnn_policy import DnnPolicy
from std_msgs.msg import String 
import pdb
import pickle
import tempfile

def cb(msg):
    rospy.loginfo('received %s'%msg)
    with open(msg.data, 'rb') as f:
        req = pickle.load(f)

    obs = req['obs']
    tgt_mu = req['tgt_mu']
    tgt_prc = req['tgt_prc']
    tgt_wt = req['tgt_wt']

    dU = tgt_mu.shape[1]

    pol = DnnPolicy(dU)
    f = tempfile.NamedTemporaryFile(delete=False, suffix='.pkl')
    pickle.dump(pol, f)
    f.close() 

    rospy.sleep(1)

    pub.publish(String(data=f.name))
    rospy.loginfo('sent %s'%f.name)
    pass

if __name__ == '__main__':
    rospy.init_node('pub_and_sub_node')
    
    rospy.Subscriber(training_request_topic, String, cb)
    pub = rospy.Publisher(training_response_topic, String)

    rospy.spin()
