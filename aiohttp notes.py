app = web.Application() # instantiates app, instantiates UrlDispatcher() class 
                        # unless we pass in a different Router

app.add_routes(routes) # calls self.router.add_routes(routes)
                       # just basically adds routes to the route table (lol)

runner = web.AppRunner(app) #Instantiates the runner object -> doesn't do much yet

await runner.setup() # setup is declared in the BaseRunner ABC
                     # gets event loop, does some stuff with signals (outside of our scope)
                     # says self._server = await self._make_server()
                     # self._make_server() gets the event loop, sets the loop on the app
                     # calls app.on_startup.freeze()
                        # Note that on_startup is an instance of the Signal(self) class
                        # This is from the aiosignal library (probably outside of our scope,
                        # but i want to find out what freeze does)
                        # freeze just prevents callbacks from happening
                    # awaits app.startup(), which calls registered call backs in the on_startup signal 
                        # (whatever that means tbh)
                    # finally, it freezes the app, which calls pre_freeze 
                        # pre_freeze just freezes a bunch of signals n stuff 
                    # and then freezes each subapp
                        # i don't think we need to know what a subapp is

site = web.TCPSite(runner) # instantiates TCPSite -> note, 
                           # it has the optional parameters host(str) and port(int)

site.start() # gets the loop, grabs the server made by the runner, uses the loop to create the server

