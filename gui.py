#!/usr/bin/env python

#import subprocess
#subprocess.Popen('roscore')

import os
#import rospy
#import roslaunch
#from revisit_planner import RevisitPlanner

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.base import EventLoop

global directory, img_path, matchings

# Parsing images with their corresponding poses
def image_locater():
    directory = os.path.dirname(os.path.realpath(__file__))
    img_path = directory + '/images/'

    try:
        if os.listdir(directory + '/images/predicted')[0].endswith('.png') or os.listdir(directory + '/images/predicted')[1].endswith('.png'):
            img_path = directory + '/images/predicted/'
    except:
        pass

    with open(img_path + 'image_pose_matchings.txt') as f:
        matchings = []
        for line in f:
            line = line.split()  
            if line:            
                line = [float(i) for i in line]
                matchings.append(line)
    return directory, img_path, matchings

directory, img_path, matchings = image_locater()

# Mapping Tab in GUI
class Mapping(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Mapping, self).__init__(*args, **kwargs)
        #self.matching_node = roslaunch.core.Node('orko', 'image_pose_matching.py')
        #self.launch = roslaunch.scriptapi.ROSLaunch()
        #self.launch.start()
        #self.process = None

    def mapping_mode(self, bool):
        """try:
            pass
        except BaseException:
            rospy.logwarn('Mapping warning')"""
        pass

    def match_image_to_pose(self, bool):
        """try:
            if bool:
                self.process = self.launch.launch(self.matching_node)
            else:
                self.process.stop()  
        except BaseException:
            pass"""
        pass

# Revisiting Tab in GUI
class Revisiting(BoxLayout):
    imagenum = len(matchings)
    img_path = img_path

    def __init__(self, *args, **kwargs):
        super(Revisiting, self).__init__(*args, **kwargs)
        """self.rp = RevisitPlanner(matchings)
        self.octomap_node = roslaunch.core.Node('orko', 'octomap_loader.py')
        self.octomap_launch = roslaunch.scriptapi.ROSLaunch()
        self.octomap_launch.start()
        self.octomap_process = None
        self.progress = 0.0
        self.progress_bar = ProgressBar(max=1.0, value=self.progress)"""
        
    def select_goal(self, image_id):
        """try:
            #popup = Popup(title='Mission Progress', title_font='Roboto-Regular', 
            #   content=self.progress_bar, auto_dismiss=True, size_hint=(1, 0.3))
            #popup.open()
            #while not self.rp.specify_goal(image_id):
            #   self.progress = self.progress + self.rp.dt
            #   print self.progress
        
            #if self.progress == 1.0:
                #popup.dismiss()
            self.rp.specify_goal(image_id)

        except BaseException:
            rospy.logwarn('Mission cannot be executed')"""
        pass

    def stop_robot(self):
        #self.rp.stop()
        pass

    def load_octomap(self):
        pass

    def predict_cracks(self):
        try:
            from crack_detection import test
            test(model_prefix='brick')
            directory, img_path, matchings = image_locater()
        except:
            pass

# Main Menu Tab in GUI
class MainMenu(TabbedPanel):
    def __init__(self, *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)
        """ self.uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(self.uuid)
        self.launch = roslaunch.parent.ROSLaunchParent(self.uuid, 
            ["~/catkin_ws/src/orko/launch/orko.launch"])
        self.streaming_node = roslaunch.core.Node('rqt_image_view', 'rqt_image_view', 
            args='/camera/rgb/image_rect_color', name='video_stream')
        self.streaming_launch = roslaunch.scriptapi.ROSLaunch()
        self.streaming_launch.start()
        self.streaming_process = None """

    def launch_ros(self, bool):
        """try:
            if bool:
                self.launch.start()
            else:
                self.launch.shutdown()
        except BaseException:
            rospy.logwarn('The launch file cannot start')"""
        pass

    def live_stream(self, bool):
        """try:
            if bool:
                self.streaming_process = self.streaming_launch.launch(self.streaming_node)
            else:
                self.streaming_process.stop()
        except BaseException:
            rospy.logwarn('Live stream cannot start')"""
        pass

    def takeoff(self):
        """from dji_sdk.srv import DroneTaskControl
        try:
            rospy.wait_for_service('/dji_sdk/drone_task_control')
            task_srv = rospy.ServiceProxy('/dji_sdk/drone_task_control', DroneTaskControl)
            task_srv(task=4)
            rospy.loginfo("Take-off")
        except rospy.ServiceException, e:
            rospy.logerr("Service call failed: %s"%e)"""
        pass

    def landing(self):
        """ from dji_sdk.srv import DroneTaskControl
        try:
            rospy.wait_for_service('/dji_sdk/drone_task_control')
            task_srv = rospy.ServiceProxy('/dji_sdk/drone_task_control', DroneTaskControl)
            task_srv(task=6)
            rospy.loginfo("Landing")
        except rospy.ServiceException, e:
            rospy.logerr("Service call failed: %s"%e) """
        pass

class PlannerInterface(BoxLayout):
    pass

# Main of GUI
class PlannerApp(App):
    def build(self):
        EventLoop.ensure_window()
        return PlannerInterface()

if __name__ == "__main__":
    try:
        #rospy.init_node('GUI')
        PlannerApp().run()
    finally:
        #rp = RevisitPlanner(matchings)
        #rp.stop()
        pass

