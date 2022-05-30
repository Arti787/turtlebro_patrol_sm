#!/usr/bin/env python

import rospy
import smach

class init_callback_service(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo("Waiting move_base action")
        if service_name:

            self.call_back_service = rospy.ServiceProxy(service_name, PatrolPointCallback)
            rospy.loginfo(f"Waiting point callback service : {service_name}")
            self.call_back_service.wait_for_service()
            rospy.loginfo(f"Init service: {service_name}")

        else:
            self.call_back_service = False
            rospy.loginfo("No point callback service")


# main
def main():
    rospy.init_node('turtlebro_patrol_sm')
    name = "Артемий"
    print(f"Hi {name}")

    sm_run = smach.StateMachine(outcomes=['shutdown'])

    with sm_run:
        # Add states to the container
        '''
        successfully. interrupted. failed.
        '''
        smach.StateMachine.add('init', init_callback_service(), 
                               transitions={'successfully':'BAR', 
                                            'interrupted':'shutdown',
                                            'failed':'shutdown'})
        smach.StateMachine.add('BAR', Bar(), 
                               transitions={'outcome2':'FOO'})

    

if __name__ == '__main__':
    main()