import argostranslate.package

FROM_CODE = "en"
TO_CODE = "pt"

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == FROM_CODE and x.to_code == TO_CODE, available_packages
    )
)
argostranslate.package.install_from_path(package_to_install.download())