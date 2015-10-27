class Buffer: 
  def _init__( self, max_wip, max_flow ):
    self.queue = 0
    self.wip = 0    # work-in-progress ("ready-pool");

    self.max_wip = max_wip
    self.max_flow = max_flow # avg outflow is max_flow/2

  def work( self, u ):
    # Add to ready pool
    u = m
