# creates a manifest that kills a process named killmenow
exec {'killmenow':
  command  => 'ps aux | grep killmenow | pkill killmenow',
  provider => 'shell',
}
