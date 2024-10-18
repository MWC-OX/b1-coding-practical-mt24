"""PD controller implementation"""


class Controller:
    """
    A Proportional-Derivative (PD) controller.

    This class implements a simple PD controller that calculates
    the control action based on the proportional and derivative
    gains, applied to the error between a desired reference
    value and the current position.

    Attributes:
        k_p (float): The proportional gain.
        k_d (float): The derivative gain.
    """

    def __init__(self, k_p: float, k_d: float):
        """
        Initializes the PD controller with specified gains.

        Args:
            k_p (float): The proportional gain.
            k_d (float): The derivative gain.
        """
        self.k_p = k_p
        self.k_d = k_d
        self.previous_err = 0

    def update_action(self, reference: float, position: float) -> float:
        """
        Calculates the control action based on the 
        reference and current position.

        Args:
            reference (float): The desired reference value.
            position (float): The current position.

        Returns:
            float: The calculated control action.
        """

        # Calculate error and action
        err = self._calc_err(reference, position)
        action = (err * self.k_p) + (self.k_d * (err - self.previous_err))

        # Updates previous error for next time step
        self.previous_err = err
        return action

    def _calc_err(self, reference: float, position: float) -> float:
        """
        Calculates the error between the reference and current position.

        Args:
            reference (float): The desired reference value.
            position (float): The current position.

        Returns:
            float: The calculated error (reference - position).
        """
        return reference - position

    def reset(self):
        """
        Resets the previous error to zero.

        This method can be used to reset the controller state
        when starting a new control process or to clear
        accumulated error history.
        """
        self.previous_err = 0
