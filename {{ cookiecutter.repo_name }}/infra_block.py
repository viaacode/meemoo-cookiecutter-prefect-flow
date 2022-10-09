from prefect.infrastructure.docker import DockerContainer, DockerRegistry
import argparse


def save_image(image_name, name, registry=None) -> None:
    docker_registry = DockerRegistry.load(registry)
    docker_container = DockerContainer(
        image=image_name,
        auto_remove=True,
        image_registry=docker_registry,
        image_pull_policy="ALWAYS",
    )
    docker_container.save(name=name, overwrite=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Save a Docker container")
    parser.add_argument("--image", required=True, help="Docker image to run")
    parser.add_argument("--name", required=True, help="Name of the block")
    parser.add_argument(
        "--registry",
        required=False,
        help="Docker registry (the block which it contains), default docker.io",
    )
    args = parser.parse_args()
    save_image(args.image, args.name, args.registry)
