from celery import shared_task


@shared_task(bind=True)
def test_func(self):
    with open("verify.txt", "a") as file:
        file.write("dump_verifycode")
    return "Done!"
