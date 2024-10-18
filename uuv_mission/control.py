

class Controller:

    def __init__(self, k_p: float, k_d: float):
        self.k_p = k_p
        self.k_d = k_d
        self.previous_err = 0

    def update_action(self, reference: float, posistion: float) -> float:
        err = self._calc_err(reference, posistion)
        action = (err * self.k_p) + (self.k_d * (err - self.previous_err))
        self.previous_err = err
        return action

    def _calc_err(self, reference: float, posistion: float) -> float:
        return reference - posistion
    
    def reset(self):
        self.previous_err = 0
