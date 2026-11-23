# /ui-review のプロジェクト設定

<!-- status: configured -->

このファイルは `/ui-review` を初めて実行したときに、リポジトリを調べて自動で埋められる。
手で直してもよい。`status` が `unconfigured` のあいだは、/ui-review は最初にこのファイルの設定を行う。

## アプリの概要

- 何のアプリか: IceFritz（AQW の Cruel ギルド）の個人サイト icefritz.me。トップ（名刺的なランディング）、AQW のブースト一覧、所持装備チェックリスト
- 主な利用者と使い方: ギルドメンバーや AQW プレイヤーが Discord / X のリンクから開く。トップは結晶をクリックしてメニューを開き、各ツールへ移動する
- 主な対象の画面幅: 両方（スマホ縦・タブレット横・デスクトップそれぞれにレイアウト調整あり）

## 技術スタック

- フレームワーク: なし（素の静的 HTML、ビルドなし。GitHub Pages、CNAME あり）
- ルーター: なし（ディレクトリごとの index.html）
- スタイリング: 素の CSS。共通は `assets/ice.css`（トークン・背景・.plate・.rune）と `assets/crystal.css`（結晶メニュー）、各ページの `<style>` に個別スタイル
- デザイントークンの場所: `assets/ice.css` の `:root`（--bg, --abyss, --navy, --steel, --slate, --frost, --muted, --ice, --ice-hi, --plate, --panel, --edge）
- フォント: Google Fonts の Silkscreen（ピクセル体、名前プレート・メニュー見出し）と Outfit 300/600（本文）
- アイコン: なし（インライン SVG の結晶とルーン円。`assets/crystal.js` が結晶メニューを生成）
- ダークモード: ダーク固定（`color-scheme: dark`、`darkreader-lock`）

## dev サーバー

- 起動コマンド: `npx serve -l 3917 .`（3000 は別プロジェクトが使うことがあるため 3917）
- ベースURL: http://localhost:3917/
- 起動確認: `curl -s -o /dev/null -w "%{http_code}" http://localhost:3917/` が 200
- ハッシュルーター: いいえ

## ビューポート

撮影するビューポート。1つ目を主とする。

| 名前      | 幅×高さ   | 用途                                   |
| --------- | --------- | -------------------------------------- |
| mobile    | 390×844   | 主（Discord / X から開く想定）         |
| mobile-sm | 360×740   | はみ出し確認                           |
| desktop   | 1440×900  | 主（デスクトップでも開かれる）         |
| tablet-l  | 1180×820  | トップのみ（iPad 横向けの持ち上げ調整あり） |

## 画面一覧

| 画面名（引数で受け付ける名前） | URL | 主なファイル | spec の capability（OpenSpec を使う場合） | change 名 |
| ------------------------------ | --- | ------------ | ----------------------------------------- | --------- |
| home / トップ                  | http://localhost:3917/ | index.html, assets/ice.css, assets/crystal.css, assets/crystal.js | - | ui-refine-home |
| boosts / ブースト              | http://localhost:3917/boosts/ | boosts/index.html, boosts/boosts.json | - | ui-refine-boosts |
| checklist / チェックリスト     | http://localhost:3917/checklist/ | checklist/index.html | - | ui-refine-checklist |

- トップは結晶メニューを開いた状態（結晶をクリック）も撮る。
- `404.html`、`test/`・`tests/` はリダイレクト用でレビュー対象外。

## データの準備

撮影用のブラウザ（Playwright）は利用者の端末とは別で、データが空のことが多い。

- 方法: home / boosts はなし（boosts は `boosts/boosts.json` を読むので空にならない）。checklist は進捗を localStorage に保存するため、撮影用ブラウザでは未チェックの状態になる
- 手順: checklist で進捗ありの状態を撮りたい場合は、撮影用ブラウザ内で項目を数件クリックしてチェックを付ける（専用のシードは今のところなし。必要になったら `.claude/skills/ui-review/fixtures/` に追加する）
- 注意: 利用者の本番データには触れない方法に限る。

## 変更の起票先

- OpenSpec: 使わない（`openspec/` ディレクトリも CLI も無い）
  - `docs/ui-reviews/ui-refine-<画面>/` に proposal.md / tasks.md / screenshots/ を書き出す。
- テスト・lint のコマンド: なし（ビルド・テストなし）。`npx serve -l 3917 .` で表示を確認する
