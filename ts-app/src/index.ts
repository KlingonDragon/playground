import './utility/prototypes';
import { _, $ } from './utility/DOM';
$('html', { classList: ['dark'] });
$('body', { classList: ['light'] })?._(
    _('header', { classList: ['dark'] })._(_('h1')._('Debug and Testing')),
    _('main',)._(
        _('div', {
            classList: ['initial-test-class'],
            dataset: { test: 'value' },
            properties: { id: 'some-id' },
            styles: { fontSize: '2rem;', color: 'red' }
        })._('Hello World!'),
        _('input', { classList: ['dark'], properties: { type: 'password', placeholder: 'password?' } })
    ),
    _('footer', { classList: ['dark'] })._('Footer content')
);
setTimeout(() => $('#some-id', { classList: ['updated-test-class'], replaceClassList: true }), 3e3)
setTimeout(() => console.log($('input', { properties: { value: 'Secret!' } })?.value), 8e3)