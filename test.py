#!/usr/bin/env python

import asyncio
import techmanpy

async def listen():
   async with techmanpy.connect_svr(robot_ip='192.168.98.251') as conn:
      conn.add_broadcast_callback(print)
      await conn.keep_alive()

asyncio.run(listen())