# How to contribute?

If you'd like to contribute resources, please read this document before sending a PR.

## Contributing Resources

If you have the infrastructure, I highly encourage you to fork this repository and maintain a different version as I
have limited storage available on my VPS, ping me if you need help setting it up. Otherwise, you can contribute here.

### Blobs

Unless strictly necessary for the build process (like images for a TeX file) avoid checking in any blobs into the source
tree. To contribute blobs, create an issue with a temporary link to the blob and also mention the desired path. I'll
then upload it to my VPS after reviewing it.

### Non-Blobs

Add your resource under the appropriate directory under the `src` directory and create a PR. Also create a `config.toml`
file if required. I'll write documentation for the site builder soon.

### Naming convention for other batches

If you're not in the IIoT 23-27 batch, follow these rules:

* **Same branch, different year:** wherever you were going to place your file nest it under a directory named after the
  year you were in that semester. For example, if you want to add a 3rd semester resource for the IIoT 22-26 batch place
  it under `sem3/subject/2023/assignment.pdf`.
* **Different branch, same year:** just create a directory named after your branch's short name (AIDS, AIML, AR) under
  any semester's directory, example: `sem6/aids/subject/resource.pdf`.
* **Different branch, different year:** same as rule 2, just add year like `sem5/aiml-2023/subject/resource.pdf`

## Meta Contributions

You can also contribute to the tools that build and maintain this site, they're located in the `utils` directory.

* Follow pep8 style guide.
* Unless you have a good reason, avoid adding dependencies.