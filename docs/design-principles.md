# デザイン方針

このアプリのUIで守るルール。/ui-review で採用した修正方針がここに蓄積される。
新しい画面やコンポーネントを作るときも、このファイルに従うこと。

- ルールは「何をどうするか」を一行で書く（例: 一覧の区切りはカードではなく1pxの罫線）。
- 各ルールの末尾に由来の change 名を付ける。
- 例外を作るときは、ルールを消さずに例外として追記する。

## 形と区切り
- 本文中の操作リンクはボックスにせず、行内に収める（ui-refine-checklist-2）
- 一覧は1列で上から下に読む。項目名は左、タグは右に流す（ui-refine-checklist）
- 操作部品の角丸は6px、タグは4px。ピル形は使わない（ui-refine-checklist）
- 一覧の種類は行の左の2pxの罫線で示す（ui-refine-boosts）
- メニュー項目は箱ではなく1pxの罫線で区切る（ui-refine-home）

## 色と階層
- 短いタグの文字は12px未満のピクセル書体にしない（ui-refine-checklist-2）
- タグの色は課金区分だけに使い、それ以外は無彩色にする（ui-refine-checklist）
- 進捗バーは単色で塗る（ui-refine-checklist）
- 見出しの区切り線は単色の1pxにする（ui-refine-boosts）
- グロー（text-shadow / drop-shadow）は結晶だけに使う（ui-refine-home）

## アイコンと文字
- 操作を示す説明文は12px以上にする（ui-refine-home）

## 余白とレイアウト
- デスクトップの固定サイドバーには閲覧用の内容だけを置き、設定・保存は折りたたむ（ui-refine-checklist-2）
- モバイルのフィルタは1行の横スクロールで出し、最初の一覧行を画面内に残す（ui-refine-checklist-2）
- 空の一覧には、次に取れる操作（フィルタ解除）を同じ場所に置く（ui-refine-checklist-2）
- モバイルでは最初の一覧行が最初の画面に入るよう、フィルタとフォームは折りたたむ（ui-refine-checklist）
- デスクトップの絞り込みは一覧のスクロールに追従させる（ui-refine-checklist）
- ライブ中の項目は残り時間を最も大きな数字として右に置き、次の予定は一覧に任せる（ui-refine-boosts）
- 一覧の補助情報（日数）は行の右端に置き、行を折り返さない（ui-refine-boosts）
- 週ごとの一覧は読む順番を上から下に保つ（グリッドで横に並べない）（ui-refine-boosts）
- 日時は分断せず、nowrap で一塊にする（ui-refine-boosts）

## 例外
