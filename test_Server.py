
import asyncio
import techmanpy

async def listen():
   async with techmanpy.connect_svr(robot_ip='192.168.98.251') as conn:
      robot_model = await conn.get_value('Joint_Angle')
      print(robot_model)
      
      # conn.add_broadcast_callback(print)
      
      await conn.keep_alive()

asyncio.run(listen())