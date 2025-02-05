//#region HTMLElement
interface HTMLElement {
    _(...nodes: (Node | string)[]): this;
    __(...nodes: (Node | string)[]): this;

    $assign<TagName extends keyof HTMLElementTagNameMap>(options: DOMOptionsComplete<TagName>): this;
}
HTMLElement.prototype._ = function (...nodes) { this.append(...nodes); return this; }
HTMLElement.prototype.__ = function (...nodes) { this.replaceChildren(...nodes); return this; }
HTMLElement.prototype.$assign = function (options) {
    if (options.replaceClassList) { this.classList.remove(...this.classList); }
    if (options.classList) this.classList.add(...options.classList);
    if (options.dataset) Object.assign(this.dataset, options.dataset);
    if (options.properties) Object.assign(this, options.properties);
    if (options.styles) Object.assign(this.style, options.styles);
    return this;
}
//#endregion

//#region Object
interface Object {
    forEach(callbackfn: (value: [string, any], index: number, array: [string, any][]) => void): void;
}
Object.prototype.forEach = function (callback) { Object.entries(this).forEach(callback); };
//#endregion