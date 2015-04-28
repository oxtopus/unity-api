import web
import json



urls = (
    '/init', 'init',
    '/sync', 'sync',
    '/crossdomain.xml', 'crossdomain',
    '/update', 'update'
)

outputNames = []
outputTypes = []
inputNames = []
inputTypes = []

outputData = {}
inputData = {}

timestep = 0



class init:
  def POST(self):
    global outputNames, outputTypes, inputNames, inputTypes
    outputNames = json.loads(web.input().outputNames)
    outputTypes = json.loads(web.input().outputTypes)
    inputNames = json.loads(web.input().outputNames)
    inputTypes = json.loads(web.input().outputTypes)



class sync:
  def POST(self):
    global outputData, timestep
    outputData = json.loads(web.input().outputData)
    # inputData["position"] = outputData["position"]
    timestep += 1
    return json.dumps(inputData)


class update:
  def POST(self):
    global inputData, timestep
    inputData = json.loads(web.input().inputData)
    outputData["timestep"] = timestep
    return json.dumps(outputData)


class crossdomain:
  def GET(self):
    with open("crossdomain.xml") as f:
      return f.read()



if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()