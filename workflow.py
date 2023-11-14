
import asyncio
import techmanpy
import keyboard

async def exitListen():
   async with techmanpy.connect_sct(robot_ip='192.168.98.251') as conn:
    #   rin_listen_node = await conn.is_listen_node_active()
        rin_listen_node = await conn.exit_listen()
        # print(rin_listen_node)
      
      # conn.add_broadcast_callback(print)
    
async def isListenActive():
   async with techmanpy.connect_sta(robot_ip='192.168.98.251') as conn:
        return await conn.is_listen_node_active()
        
      

# asyncio.run(listen())

flag = 0
switch = True

while switch:
    if keyboard.is_pressed('q'):
        switch = False

    try:
        b = asyncio.run(isListenActive())
    except:
        b = False

    if b == True: 
        if flag == 0:
            flag = 1
            print("Hooray")
            #first camera call goes here
            try:
                if asyncio.run(isListenActive()):
                    asyncio.run(exitListen())
            except:
                continue
            
        elif flag == 1:
            flag = 0
            print("Hurrah again")
            #second camera call
            try:
                if asyncio.run(isListenActive()):
                    asyncio.run(exitListen())
            except:
                continue
            # asyncio.run(exitListen())
            
    
    




