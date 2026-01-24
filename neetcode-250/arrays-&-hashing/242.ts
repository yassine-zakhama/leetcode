function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) {
    return false;
  }

  const sCharCount = new Map<string, number>();
  for (let c of s) {
    const curr = sCharCount.get(c) ?? 0;
    sCharCount.set(c, curr + 1);
  }

  for (let c of t) {
    const count = sCharCount.get(c);
    if (!count) {
      return false;
    }
    sCharCount.set(c, count - 1);
  }

  return true;
}
