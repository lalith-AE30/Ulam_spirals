import create_image

def main():
    import cli
    create_image.create(cli.res,cli.scale)

if __name__=='__main__':
    main()