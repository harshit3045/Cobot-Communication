#!/usr/bin/env python

import asyncio
import techmanpy


async def move():
   async with techmanpy.connect_sct(robot_ip='192.168.98.251') as conn:
      await conn.move_to_joint_angles_ptp([10, -10, 10, -10, 10, 10], 0.80, 200)
      

asyncio.run(move())