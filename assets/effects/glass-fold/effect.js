// glass-fold: panes of glass folded over each other, each with one lit crease, screened together.
// The 0x Labs "Glass Fold" background (GradFlow, https://gradflow.meerbahadin.dev, brought in by the
// team as a 21st.dev prompt and first used on the 0x Labs site), ported to the kit's fx runtime so it
// gets the pause button, the off-screen release, the still frame under reduced motion and a CSS
// fallback without WebGL. Colours come from the page palette: the accent for the panes, the ground
// for the background, a light tint of the accent for the lit edges.
import { shader, color } from '../fx.js';

const params = {
  speed: { default: 0.35, min: 0, max: 1.5, step: 0.01 },  // 0.35 is the speed the 0x Labs site uses
  scale: { default: 1, min: 0.4, max: 2.5, step: 0.01 },   // how tightly the folds are packed
  noise: { default: 0.1, min: 0, max: 0.5, step: 0.01 },   // film grain
  glow:  { default: 0.85, min: 0.2, max: 1.2, step: 0.01 }, // how strong the panes are over the ground
};

const frag = /* glsl */ `
float gf_grain(vec2 st) { return fract(sin(dot(st, vec2(12.9898, 78.233))) * 43758.5453); }
vec2 gf_centered(vec2 uv) { vec2 p = uv - 0.5; p.x *= u_res.x / max(u_res.y, 1.0); return p; }
mat2 gf_rot(float a) { float s = sin(a); float c = cos(a); return mat2(c, -s, s, c); }

vec3 gf_shade(vec2 uv, float time) {
  vec2 q = gf_rot(0.6) * gf_centered(uv) * 2.0 * u_scale;
  float t = time * 0.6;
  float pixel = 2.0 * u_scale / max(u_res.y, 1.0);
  vec3 color = mix(u_c2g, u_c2g * 0.45, clamp(length(gf_centered(uv)) * 1.3, 0.0, 1.0));
  for (int i = 0; i < 6; i++) {
    float fi = float(i);
    float bend = mod(fi, 2.0) * 2.0 - 1.0;
    float crease = (fi - 2.5) * 0.4
                 + 0.26 * sin(q.x * (1.05 + 0.12 * fi) + fi * 1.9 + t * (0.25 + 0.05 * fi))
                 + 0.1 * bend * q.x * q.x;
    float s = q.y - crease;
    float pane = smoothstep(-pixel, pixel, s);
    float back = max(s, 0.0);
    float body = exp(-back * 1.7);
    float fresnel = exp(-back * 8.0);
    float rim = exp(-back * 80.0);
    float inner = exp(-pow((back - 0.045) / 0.014, 2.0));
    float bloom = exp(-abs(s) * 20.0);
    vec3 tint = mix(u_c1g, u_c3g, clamp(fresnel * 0.6 + 0.08 + 0.14 * sin(fi * 2.1 + q.x * 0.8 + t * 0.2), 0.0, 1.0));
    vec3 light = tint * pane * (body * 0.42 + fresnel * 0.4)
               + u_c3g * (pane * (rim * 0.6 + inner * 0.12) + bloom * 0.1);
    color += light * u_glow * (1.0 - color);
  }
  return clamp(color, 0.0, 1.0);
}

void main() {
  vec2 uv = fx_uv();
  float time = u_time * u_speed + u_seed * 0.013;
  vec3 col = gf_shade(uv, time);
  if (u_noise > 0.001) {
    float g = gf_grain(uv * 200.0 + u_time * 0.1);
    col *= 1.0 - u_noise * 0.4 + u_noise * g * 0.4;
  }
  fxColor = vec4(col, 1.0);
}
`;

const rgb = hex => {
  const h = String(hex).replace('#', '');
  const f = h.length === 3 ? h.split('').map(c => c + c).join('') : h.slice(0, 6);
  const n = parseInt(f, 16);
  return [((n >> 16) & 255) / 255, ((n >> 8) & 255) / 255, (n & 255) / 255];
};

// panes in a deeper step of the accent, the ground a step under the page, the edges a light tint
function tones(P) {
  const pane = color.mix(P.accent, P.bg, 0.35);
  const ground = color.mix(P.bg, '#000000', 0.25);
  const edge = color.mix(P.accent, '#ffffff', 0.55);
  return { pane, ground, edge };
}

export default {
  id: 'glass-fold',
  name: 'Glass fold',
  family: 'material',
  params,
  mount(el, { palette, params: given, seed }) {
    return shader(el, {
      frag,
      schema: params,
      params: given,
      palette,
      seed,
      maxDpr: 1,
      still: 4,
      uniforms: ({ palette: P }) => {
        const T = tones(P);
        return { u_c1g: rgb(T.pane), u_c2g: rgb(T.ground), u_c3g: rgb(T.edge) };
      },
      fallback: ({ palette: P }) => {
        const T = tones(P);
        return `linear-gradient(160deg, ${T.ground} 0 30%, ${T.pane} 55%, ${T.edge} 62%, ${T.pane} 70%, ${T.ground} 100%)`;
      },
    });
  },
};
