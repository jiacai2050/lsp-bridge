from core.handler import Handler
from core.utils import *
from typing import Union
import json

class ExpandMacro(Handler):
    name = "expand_macro"
    method = "rust-analyzer/expandMacro"
    cancel_on_change = True

    def process_request(self, position) -> dict:
        self.pos = position
        return dict(position=position)

    def process_response(self, response: Union[dict, list]) -> None:
        # find_define_response(self, response, "lsp-bridge-define--jump")
        eval_in_emacs("lsp-bridge-rust-expand-macro-callback", response["name"], response["expansion"])
