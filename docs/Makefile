# We check if live-server and tailwindcss-cli are in the user's $PATH
# If they are present there is no need to use npx
# we could just run the executables directly
ifeq (, $(shell type live-server 2> /dev/null))
NPX = npx
else ifeq (, $(shell type tailwindcss-cli 2> /dev/null))
NPX = npx
else
NPX =
endif

help:
	@printf "%b" "Welcome! You've started the Blendicons build configurer! \n"
	@printf "%b" "Here are the build options: \n"
	@printf "%b" "- make help (default) \n"
	@printf "%b" "- make dev \n"
	@printf "%b" "- make build \n"
	@printf "%b" "- make serve \n"
	@printf "%b" "- make dist \n"
	@printf "%b" "- make generate \n"

dev:
	@printf "%b" "\033[1;35m• Preparing CSS assets...\033[0m \n"
	@${NPX} tailwindcss-cli@latest -i ./css/raw/tailwind.css -o ./css/build/tailwind.output.css
	@printf "%b" "\033[32m(✓) Compilation finished successfully\033[0m \n"

build:
	@printf "%b" "\033[1;35m• Preparing CSS assets...\033[0m \n"
	@export NODE_ENV='production' && ${NPX} tailwindcss-cli@latest -i ./css/raw/tailwind.css -o ./css/build/tailwind.output.css
	@printf "%b" "\033[32m(✓) Compilation finished successfully\033[0m \n"

serve:
	@printf "%b" "\033[1;36m• Starting live development server...\033[0m \n"
	@${NPX} live-server

dist:
	@printf "%b" "\033[1;35m• Bundling CSS assets...\033[0m \n"
	@printf "%b" "\033[1;32m• Tree-shaking unused styles...\033[0m \n"
	@export NODE_ENV='production' && ${NPX} tailwindcss-cli@latest -i ./css/raw/tailwind.css -o ./css/build/tailwind.output.css
	@printf "%b" "\033[32m(✓) Done! Preparing live server to serve assets.\033[0m \n"
	@read -p "Press ENTER to start server, or CTRL C to stop: "
	@${NPX} live-server

generate:
	@python docs_generate.py
	echo Done! Generated pages, ready to serve.
