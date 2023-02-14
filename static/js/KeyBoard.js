const TabKeyBoard = (floor, DownTerminal) => {
    const floorTerminal = document.getElementById(floor);
    const downTerminal = document.getElementById(DownTerminal);
    const value = downTerminal.textContent;

    const downTerminalAction = () => {
      let valueFloor = floorTerminal.textContent;
      valueFloor === "_"
        ? (floorTerminal.innerText = "")
        : (floorTerminal.innerText = "_");
    };

    const ConfirmValueCode = () => {
      downTerminal.textContent === "yes"
        ? (window.location.href = "/login")
        : (window.location.href = "/");
    };

    const FilterValueConfirmDelete = () => {
      let valueInner = downTerminal.innerText;
      downTerminal.innerText = valueInner.substring(0, valueInner.length - 1);
    };

    const AddWrite = (letter) => {
      downTerminal.innerText += letter.length === 1 ? letter : "";
    };

    const documentKeyUp = () => {
      document.addEventListener("keyup", (e) => {
        let valueTemp = "";
        if (value.length === 10) {
          downTerminal.innerText = valueTemp;
        }
        valueTemp = value;
        funcKeyUp(e);
      });
    };

    const sep = () => {
      downTerminal.innerText += "\u00a0";
    };

    const funcKeyUp = (event) => {
      let code = event.code;
      let letterCode = event.key;
      switch (code) {
        case "Enter":
          ConfirmValueCode();
          break;
        case "Space":
          sep();
          break;
        case "Backspace":
          FilterValueConfirmDelete();
          break;
        default:
          AddWrite(letterCode);
          break;
      }
    };
    documentKeyUp();
    setInterval(downTerminalAction, 300);
  };