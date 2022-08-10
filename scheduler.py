from rocketry import Rocketry


app = Rocketry()

@app.task('every 2 s', execution='process')
def madoka_magic():
    print("magic!")

if __name__ == "__main__":
    app.run()
