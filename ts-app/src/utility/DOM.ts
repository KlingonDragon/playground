import './prototypes';
//#region _
export function _<TagName extends keyof HTMLElementTagNameMap>(tagName: TagName, options?: DOMOptionsWithProperties<TagName>): HTMLElementTagNameMap[TagName] {
    const newElement = document.createElement(tagName);
    if (options) { newElement.$assign(options) }
    return newElement
}
//#endregion

//#region $
export function $<Selector extends keyof HTMLElementTagNameMap>(selector: Selector, options?: DOMOptionsComplete<Selector>): HTMLElementTagNameMap[Selector] | null;
export function $(selectors: string, options?: DOMOptionsWithReplaceClassList): HTMLElement | null;
export function $<Selector extends keyof HTMLElementTagNameMap>(selector: Selector, options?: DOMOptionsComplete<Selector>): HTMLElementTagNameMap[Selector] | null {
    const selectedElement = document.querySelector(selector)
    if (selectedElement && options) { selectedElement.$assign(options) }
    return selectedElement;
}
//#endregion

//#region $$
export function $$<Selector extends keyof HTMLElementTagNameMap>(selectors: Selector): NodeListOf<HTMLElementTagNameMap[Selector]>
export function $$(selectors: string): NodeListOf<HTMLElement>
export function $$<Selector extends keyof HTMLElementTagNameMap>(selectors: Selector): NodeListOf<HTMLElementTagNameMap[Selector]> {
    return document.querySelectorAll(selectors);
}
//#endregion