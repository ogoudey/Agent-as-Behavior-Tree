import bt_library as btl




class SpotCleaning(btl.Condition):
    """
    Implementation of the condition "spot cleaning".
    """

    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('SpotCleaning')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Checking Request for Spot Cleaning')
        
        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(SPOT_CLEANING, 0) \
            else self.report_failed(blackboard)
            
class GeneralCleaning(btl.Condition):
    """
    Implementation of the condition "general cleaning".
    """

    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('GeneralCleaning')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Checking Request for General Cleaning')
        

        
        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(GENERAL_CLEANING, 0) \
            else self.report_failed(blackboard)
