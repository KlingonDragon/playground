interface DOMOptions {
    classList?: string[],
    dataset?: { [key: string]: string },
    styles?: Partial<CSSStyleDeclaration>
}
interface DOMProperties<TagName extends keyof HTMLElementTagNameMap> {
    properties?: Partial<HTMLElementTagNameMap[TagName]>
}
interface DOMReplaceClassList {
    replaceClassList?: boolean;
}
type DOMOptionsWithProperties<TagName extends keyof HTMLElementTagNameMap> = DOMOptions & DOMProperties<TagName>;
type DOMOptionsWithReplaceClassList = DOMOptions & DOMReplaceClassList;
type DOMOptionsComplete<TagName extends keyof HTMLElementTagNameMap> = DOMOptions & DOMProperties<TagName> & DOMReplaceClassList;
